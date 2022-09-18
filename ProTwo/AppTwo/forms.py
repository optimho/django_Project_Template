from django import forms
from AppTwo.models import User_List

class UserDetails(forms.ModelForm):
    # u_name = forms.CharField()
    # u_email = forms.EmailField()
    # u_text = forms.CharField(widget=forms.Textarea)


    class Meta():
        model = User_List
        fields = "__all__"


