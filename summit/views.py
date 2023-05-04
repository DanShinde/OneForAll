from django.shortcuts import render, redirect, get_object_or_404
from .forms import SummitForm
from .models import SummitData
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect

@user_passes_test(lambda user: user.groups.filter(name='timesheet').exists())
@login_required
def summit_form(request, summit_id=None):
    summit_data = get_object_or_404(SummitData, id=summit_id) if summit_id else None
    form = SummitForm(request.POST or None, instance=summit_data)
    if form.is_valid():
        summit_data = form.save(commit=False)
        summit_username = form.cleaned_data['summit_username']
        weekdays = form.cleaned_data['weekday']
        summit_data.user = request.user
        if SummitData.objects.filter(summit_username=summit_username).exclude(id=summit_data.id).exists():
            form.add_error('summit_username', 'This Summit username is already in use')
            context = {
                'form': form,
                'summit_data': summit_data,
            }
            return render(request, 'summit/form.html', context)
        summit_data.summit_username = summit_username
        summit_data.weekdays = weekdays
        print(summit_data.weekdays)
        summit_data.save()
        return redirect('summit-list')
    context = {
        'form': form,
        'summit_data': summit_data,
    }
    return render(request, 'summit/form.html', context)

class SummitDataListView(LoginRequiredMixin, ListView):
    model = SummitData
    template_name = 'summit/list.html'

    def get_queryset(self):
        return SummitData.objects.filter(user=self.request.user)
        
class SummitDataUpdateView(LoginRequiredMixin, UpdateView):
    model = SummitData
    form_class = SummitForm
    template_name = 'summit/form.html'
    success_url ="/summit/list/"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    def form_valid(self, form):
        # Get the instance of the model being edited
        self.object = form.save(commit=False)
        
        # Get the selected weekdays from the form and save them to the model
        weekdays = self.request.POST.getlist('weekday')
        self.object.weekdays = weekdays

        # Save the model instance and redirect to the success URL
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['form'] = self.form_class(self.request.POST, instance=self.object)
        else:
            context['form'] = self.form_class(instance=self.object)
        return context


class SummitDataDeleteView(LoginRequiredMixin, DeleteView):
    model = SummitData
    success_url = reverse_lazy('summit-list')
    template_name = 'summit/confirm_delete.html'

    def get_queryset(self):
        return SummitData.objects.filter(user=self.request.user)

    def get_success_url(self):
        return self.success_url


from rest_framework import generics, permissions
from .models import SummitData
from .serializers import SummitDataSerializer

class SummitDataList(generics.ListCreateAPIView):
    queryset = SummitData.objects.all()
    serializer_class = SummitDataSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SummitDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SummitData.objects.all()
    serializer_class = SummitDataSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
