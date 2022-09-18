from django import forms


class ForName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    test = forms.CharField(widget=forms.Textarea)


    