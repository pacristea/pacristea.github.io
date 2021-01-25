from django import forms
from .models import Mani, Extra, Pedi

class ManiForm(forms.Form):
    service_title = forms.ModelChoiceField(widget=forms.RadioSelect(attrs={'class': 'serviceForm'}), label='Bitte whälen Sie Ihre Packet', queryset=Mani.objects.all())

class PediForm(forms.Form):
    service_title = forms.ModelChoiceField(widget=forms.RadioSelect(attrs={'class': 'serviceForm'}), label='Bitte whälen Sie Ihre Packet', queryset=Pedi.objects.all())

class ExtraForm(forms.Form):
    extra_title = forms.ModelChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'serviceForm'}), label='Bitte whälen Sie Ihre Extra', queryset=Extra.objects.all())