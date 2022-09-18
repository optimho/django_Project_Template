from django.shortcuts import render
from django.shortcuts import HttpResponse
from AppTwo.models import User_List
from . import forms
# Create your views here.

def index(request):

    page_data_dictionary = {'data_1': "Home Page"}
    return render(request, 'AppTwo/help.html', context=page_data_dictionary)

def users(request):
    theusers = User_List.objects.order_by('first_name')
    user_dictionary = {'user_list': theusers}
    for item in user_dictionary:
        print(item)
    # page_data_dictionary = {'data_1': "Help File"}
    return render(request, 'AppTwo/users.html', context=user_dictionary)


def userDetails(request):
    registrationform = forms.UserDetails()

    if request.method == 'POST':
        registrationform=forms.UserDetails(request.POST)

        if registrationform.is_valid():
            #do something
            print("Form Validation success")
            print("Name " + registrationform.cleaned_data['u_name'])
            print("Email " + registrationform.cleaned_data['u_email'])
            print("Text " + registrationform.cleaned_data['u_text'])


    return render(request, 'AppTwo/registration.html', {'registration': registrationform})


