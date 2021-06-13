from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.views.generic.edit import ModelFormMixin,ProcessFormView
from .models import TodoModel
from todoapp.forms import TodoForm
# Create your views here.


class TodoListView(ListView,ModelFormMixin):
    form_class = TodoForm
    context_object_name = 'contents'
    template_name = 'todoapp/index.html'
    queryset = TodoModel.objects.all().order_by('-published')

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        return ListView.get(self, request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        return context
    
class TodoDetailView(DetailView):
    model = TodoModel
    context_object_name = 'todo'
    template_name='todoapp/detail_page.html'

class TodoUpdateView(UpdateView):
    model = TodoModel
    form_class = TodoForm
    template_name = 'todoapp/update_page.html'
    success_url = reverse_lazy('mytodolist')

class TodoDeleteView(DeleteView):
    model = TodoModel
    success_url = reverse_lazy('mytodolist')