from django.shortcuts import render, redirect
from .forms import ReservaForm
from .models import Reserva
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

@login_required
def criar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.user = request.user
            reserva.save()
            return redirect('minhas_reservas')
    else:
        form = ReservaForm()
    return render(request, 'reservas/criar_reserva.html', {'form': form})

@login_required
def minhas_reservas(request):
    reservas = Reserva.objects.filter(user=request.user)
    return render(request, 'reservas/minhas_reservas.html', {'reservas': reservas})


