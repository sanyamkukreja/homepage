from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homesite(request):
    return render(request,'home.html')

def puncation(request):
    return HttpResponse("remove punc")   