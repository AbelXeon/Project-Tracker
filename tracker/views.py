from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Project
from django.db.models import Count

class ProjectListView(ListView):
    model = Project
    template_name = 'tracker/project_list.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stats = Project.objects.values('status').annotate(count=Count('id'))
        context['labels'] = [s['status'] for s in stats]
        context['counts'] = [s['count'] for s in stats]
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'tracker/project_detail.html'

class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'description', 'technology', 'status', 'what_i_learned']
    template_name = 'tracker/project_form.html'
    success_url = reverse_lazy('project_list')

class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['name', 'description', 'technology', 'status', 'what_i_learned']
    template_name = 'tracker/project_form.html'
    success_url = reverse_lazy('project_list')

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'tracker/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')
