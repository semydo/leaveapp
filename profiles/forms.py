from django.forms import ModelForm
from .models import *


class BiodataForm(ModelForm):
    class Meta:
        model = Biodata
        fields = '__all__'


class EmploymentDetailsForm(ModelForm):
    class Meta:
        model = EmploymentDetails
        fields = '__all__'
