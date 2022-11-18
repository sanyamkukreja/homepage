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
        return render(request,'sync.html',params)
    elif(fullcap=="on"):
        syncword=""
        for char in djtext:
            syncword=syncword+char.upper()
        scoop={'purpose':'uppercase','printtype':syncword}
        return render(request,'sync.html',scoop)

    elif(remover=="on"):
        line=""
        for char in djtext:
            if char!='\n':
                line=line + char
        pogo={'purpose':'lineremover','effect':line}
        return render(request,'sync.html',pogo)
    elif(spacetype=='on'):
        spoke=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                
                spoke=spoke+char
        past={'purpose':'removedline','effectthis':spoke}

        return render(request,'sync.html',past)
    elif(count=="on"):
        code=0
        for index in range(len(djtext)):
            if not(djtext[index]==" "):
                code=code+1
        sep={'purpose':"countwords",'typeshit':code}
        return render(request,'sync.html',sep)               
    else:
        return HttpResponse("error")          