from django import forms

class OrderForm(forms.Form):
    name_surname = forms.CharField(max_length=200)
    age = forms.CharField(max_length=100)
    location = forms.CharField(max_length=200)
    circumstances = forms.CharField(max_length=200)
    additional_info = forms.CharField(max_length=200)