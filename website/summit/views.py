from django.shortcuts import render, redirect, get_object_or_404
from .forms import SummitForm
from .models import SummitData
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict

@user_passes_test(lambda user: user.groups.filter(name='timesheet').exists())
@login_required
def summit_form(request, summit_id=None):
    summit_data = get_object_or_404(SummitData, id=summit_id) if summit_id else None
    form = SummitForm(request.POST or None, instance=summit_data)
    if form.is_valid():
        summit_data = form.save(commit=False)
        summit_username = form.cleaned_data['summit_username']
        summit_data.user = request.user
        if SummitData.objects.filter(summit_username=summit_username).exclude(id=summit_data.id).exists():
            form.add_error('summit_username', 'This Summit username is already in use')
            context = {
                'form': form,
                'summit_data': summit_data,
            }
            return render(request, 'summit/form.html', context)
        summit_data.summit_username = summit_username
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

class SummitDataDeleteView(LoginRequiredMixin, DeleteView):
    model = SummitData
    success_url = reverse_lazy('summit-list')
    template_name = 'summit/confirm_delete.html'

    def get_queryset(self):
        return SummitData.objects.filter(user=self.request.user)

    def get_success_url(self):
        return self.success_url

