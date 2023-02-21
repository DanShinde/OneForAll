from django.shortcuts import render, redirect, get_object_or_404
from .forms import SummitForm
from .models import SummitData
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

@login_required
def summit_form(request, summit_id=None):
    summit_data = get_object_or_404(SummitData, id=summit_id) if summit_id else None
    form = SummitForm(request.POST or None, instance=summit_data)
    if form.is_valid():
        summit_data = form.save(commit=False)
        summit_username = form.cleaned_data['summit_username']
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

@login_required
class SummitDataListView(ListView):
    model = SummitData
    template_name = 'summit/list.html'