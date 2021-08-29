from django.shortcuts import render, HttpResponse
# Create your views here.

def News(request):
    return render(request, 'News/News.html')

def Newsposts(request, slug):
    return HttpResponse(f'Newsposts: {slug}')