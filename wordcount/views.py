from django.http import HttpResponse # for returning string
from django.shortcuts import render # for html
import operator


def home(request):
    return HttpResponse('Hello')
'''
# This implementation is for understanding templates
def homepage(request):
    return render(request,'home.html',{'hithere' : 'This is me'})
'''
def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            # Increase
            worddictionary[word]+=1
        else:
            # Add to worddictionary
            worddictionary[word]=1
    sortedwords=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext , 'wordcount' : len(wordlist) , 'sortedwords' : sortedwords})
def about(request):
    return render(request,'about.html')

def python(request):
    return HttpResponse('Python is my favourite')

def html(request):
    return HttpResponse('<h1>This is HTML output</h1>')
