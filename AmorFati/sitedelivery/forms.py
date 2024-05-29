from django.forms import ModelForm

from AmorFati.sitedelivery.models import Tarefa


class TarefaNovaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome']


