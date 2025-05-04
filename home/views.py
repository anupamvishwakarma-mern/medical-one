from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home.html')

def entry_form(request):
    return render(request, 'entry.html')