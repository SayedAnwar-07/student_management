from django.shortcuts import render

# Create your views here.
def home(request):
      return render(request, 'base.html')
def hero(request):
      return render(request, 'hero.html')
