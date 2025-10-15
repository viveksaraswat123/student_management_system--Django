from django.http import HttpResponse

def home(request):
  return HttpResponse("<h1>Welcome to first Django Projet: Home page</h1>")

def about(request):
  return HttpResponse("<h1>Welcome to about secetion: About page</h1>")

def contact(request):
  return HttpResponse("<h1>Welcome to Chai's contact section: Contact page</h1>")