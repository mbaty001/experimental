from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

#def index(request):
#    ''' Reviews entry point'''
#    name = request.GET.get("name") or "world"
#    context = {'name': name}
#    return render(request, 'reviews/base.html', context)

def search(request):
    ''' Search '''
    search = request.GET.get("search")
    context = {'search': search}
    return render(request, 'reviews/search.html', context)

def welcome_view(request):
    message = f"<html><ht>Welcome to Bookr!</h1>"\
        f"<p>{Book.objects.count()} books and counting!<p></html>"
    return HttpResponse(message)