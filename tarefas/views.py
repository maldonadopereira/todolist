from django.shortcuts import render
from django.urls import reverse

from tarefas.forms import TarefaNovaForm
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tarefas:home'))
        else:
            return render(request, 'tarefas.html', {'form': form}, status=400)
    return render(request, 'tarefas.html')