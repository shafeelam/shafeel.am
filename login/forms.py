from django.forms import ModelForm
from .models import messages

class messageForm(ModelForm):
    class Meta:
        model = messages
        fields = '__all__'