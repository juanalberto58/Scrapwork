from django import forms

class workScrapForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)