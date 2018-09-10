from django.http import HttpResponse
from django.shortcuts import render


from django.views.generic import TemplateView


#def index(request):
#    return render(request, "index.html")
class HomePageView(TemplateView):
    template_name = 'home.html'

def signin(request):
    return render(request, "signin.html")

def join(request):
    #return HttpResponse("Second page")
    return render(request, "join.html")
