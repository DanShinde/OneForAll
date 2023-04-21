"""from django.shortcuts import render
from .models import Project

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    tasks = project.tasks.all()
    return render(request, 'project_detail.html', {'project': project, 'tasks': tasks})
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Project, Task

class ProjectList(ListView):
    model = Project
    template_name = 'dms/project_list.html'

class ProjectCreate(CreateView):
    model = Project
    fields = ['name', 'description', 'assigned_to']
    success_url = reverse_lazy('dms:project_list')
    template_name = 'dms/project_form.html'

class ProjectDetail(DetailView):
    model = Project
    template_name = 'dms/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = self.object.tasks.all()
        context['tasks'] = tasks
        return context

def request_validation(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_validation_requested = True
    task.save()
    return redirect('project_detail', pk=task.project.pk)


class ProjectUpdate(UpdateView):
    model = Project
    fields = ['name', 'description', 'assigned_to']
    template_name = 'dms/project_form.html'

class ProjectDelete(DeleteView):
    model = Project
    template_name = 'dms/project_confirm_delete.html'
    success_url = reverse_lazy('dms:project_list')
