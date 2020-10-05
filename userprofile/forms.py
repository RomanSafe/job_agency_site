from django import forms


class ItemDescriptionForm(forms.Form):
    description = forms.CharField(label='Description', max_length=1024)
