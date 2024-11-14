from django import forms

class workScrap(forms.Form):
    name = forms.CharField(label='name', max_length=100)