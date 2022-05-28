from django.shortcuts import render

# Create your views here.

def index(request):
    title='Art gallore'
    return render(request, 'photo/index.html', locals())

