# forms.py
from django import forms

class NameForm(forms.Form):
    name = forms.CharField(max_length=100)

class UserInputForm(forms.Form):
    userInput = forms.CharField(max_length=100)
