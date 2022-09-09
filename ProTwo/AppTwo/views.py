from django.shortcuts import render
from django.shortcuts import HttpResponse
from AppTwo.models import User_List

# Create your views here.

def index(request):

    page_data_dictionary = {'data_1': "got to /users to see the list of users"}
    return render(request, 'AppTwo/help.html', context=page_data_dictionary)

def users(request):
    theusers = User_List.objects.order_by('first_name')
    user_dictionary = {'user_list': theusers}
    for item in user_dictionary:
        print(item)
    # page_data_dictionary = {'data_1': "Help File"}
    return render(request, 'AppTwo/users.html', context=user_dictionary)