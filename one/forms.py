from django.forms import ModelForm
from .models import enquiry

class enquiryForm(ModelForm):
    class Meta:
        model = enquiry
        fields = '__all__'