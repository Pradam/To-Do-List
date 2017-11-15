from django.shortcuts import get_object_or_404
from django.shortcuts import (render,)
from django.http import (HttpResponseRedirect,)
from django.views.generic import ListView
from .forms import (ToDoWorkForm,)
from .models import (ToDoWork,)
# Create your views here.


class ToDoWorkList(ListView):
    """List all the To Do list."""

    queryset = ToDoWork.objects.all().order_by('-id')
    template_name = 'index.html'


def todo_new(request):
    """Function to Create New To Do Object."""
    if request.method == "POST":
        form = ToDoWorkForm(request.POST)
        if form.is_valid():
            to_ = form.save(commit=False)
            to_.save()
            return HttpResponseRedirect('/')
    else:
        form = ToDoWorkForm()
    return render(request, 'add_todolist.html', {'form': form})


def todo_edit(request, pk):
    """Function to Edit To Do Object."""
    todo_post = get_object_or_404(ToDoWork, pk=pk)
    if request.method == "POST":
        form = ToDoWorkForm(request.POST, instance=todo_post)
        if form.is_valid():
            to_ = form.save(commit=False)
            to_.save()
            return HttpResponseRedirect('/')
    else:
        form = ToDoWorkForm(instance=todo_post)
    return render(request, 'edit_todolist.html', {'form': form})


def todo_delete(request, pk):
    """Function to Edit To Do Object."""
    todo_post = get_object_or_404(ToDoWork, pk=pk)
    todo_post.delete()
    return HttpResponseRedirect('/')