# from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse

# def homePageView(request):
#     return HttpResponse("Hello world")


from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'