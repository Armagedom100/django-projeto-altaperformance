from django.shortcuts import render
from django.http import HttpResponseRedirect
from AmorFati.sitedelivery.forms import TarefaNovaForm
from django.urls import reverse

def home(request):
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('sitedelivery:home'))
        else:
            return render(request, 'tarefas/home.html', {'form': form}, status=400)
    else:
        form = TarefaNovaForm()

    return render(request, 'tarefas/home.html', {'form': form})



##def home(request):
##    return HttpResponse('sitedelivery')