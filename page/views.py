from codecs import charmap_build
from string import punctuation
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homesite(request):
    return render(request,'home.html')

def puncation(request):
    #print(request.GET.get('texttype','default'))
    djtext=request.POST.get('texttype','default')
    remove=request.POST.get('puke','default')
    print(remove)
    fullcap=request.POST.get('fullcaps','off')
    remover=request.POST.get('lineremover','off')
    spacetype=request.POST.get('spaceremover','off')
    count=request.POST.get('countword','off')
    #return HttpResponse("remove punc")
    #analyzed=djtext
    if remove == "on":
        punctuations="""!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"""
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'removedpuncation','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'sync.html',params)
    if(fullcap=="on"):
        syncword=""
        for char in djtext:
            syncword=syncword+char.upper()
        scoop={'purpose':'uppercase','printtype':syncword}
        djtext=syncword
        #return render(request,'sync.html',scoop)

    if(remover=="on"):
        line=""
        for char in djtext:
            if char!='\n' and char!='\r':
                line=line + char
        pogo={'purpose':'lineremover','effect':line}
        djtext=line
        #return render(request,'sync.html',pogo)
    if(spacetype=='on'):
        spoke=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                
                spoke=spoke+char
        past={'purpose':'removedline','effectthis':spoke}
        djtext=spoke
        #return render(request,'sync.html',past)
    if(count=="on"):
        code=0
        for index in range(len(djtext)):
            if not(djtext[index]==" "):
                code=code+1
        sep={'purpose':"countwords",'typeshit':code}
        djtext=code
        #return render(request,'sync.html',sep)
        return render(request,'sync.html',djtext)               
    else:
        return HttpResponse("error")          