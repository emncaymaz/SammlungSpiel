from django.forms import ModelForm
from .models import *

class GameForm(ModelForm):

    class Meta:
        model = Game
        fields = '__all__'