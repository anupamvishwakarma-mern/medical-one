from django.shortcuts import render

# Create your views here.
def UserLogin(request):
    return render(request, 'userslogin.html')

def UserSignup(request):
    return render(request, 'usersignup.html')