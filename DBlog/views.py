from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello , Django Web Framework")

def about(request):
    return HttpResponse("About this project.")

def contact(request):
    return HttpResponse("Contact page.")

def persons(request):
    return HttpResponse("Persons here.")

