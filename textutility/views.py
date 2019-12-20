#I have created this file juned

from django.http import HttpResponse
from django.shortcuts import render 

def ex1(request):
	s ='''<h2>Navigation Bar</h2>
		<a href="https://www.youtube.com/watch?v=lcpqpxVowU0">Harry Bhaii</a><br>

		<a href="https://junedr375.github.io">StudyGuide</a>

	'''
	return HttpResponse(s)
def index2(request):
	return render(request,'index2.html')
def analyze(request):
	#get the text
	djtext=request.POST.get('text','default')
	#checkbox value
	removepunc=request.POST.get('removepunc','default')
	fullcaps=request.POST.get('fullcaps','default')
	newlineremover=request.POST.get('newlineremover','default')
	extraspaceremover=request.POST.get('extraspaceremover','default')
	counter=request.POST.get('counter','default')
	
	#Check whichh checkbox is on
	if removepunc=="on":
		#analyzed=djtext
		punctuations='''!()-{}[];:"\,<>/?@#$%^&*_~'''
		analyzed=""
		for char in djtext:
			if char not in punctuations:
				analyzed=analyzed+char
		juned={'purpose':'removepunctuation','analyzed_text':analyzed}
		djtext=analyzed
	
	if(fullcaps=="on"):
		analyzed=""
		for char in djtext:
			analyzed=analyzed+char.upper()
		juned={'purpose':'changed to upper case','analyzed_text':analyzed}
		djtext=analyzed
	

	if(newlineremover=="on"):
		analyzed=""
		for char in djtext:
			if char !="\n":

				analyzed=analyzed+char
		juned={'purpose':'removed new lines','analyzed_text':analyzed}
		#Analyzed the text
		djtext=analyzed
		#return render(request,'analyze.html',juned)

	if(extraspaceremover=="on"):
		analyzed= ""
		for index, char in enumerate(djtext):
			if djtext[index] ==" " and djtext[index+1]==" ":
				analyzed=analyzed+char
		juned={'purpose':'REmove extra Space','analyzed_text':analyzed}
		djtext=analyzed
		#Analyzed the text
		#return render(request,'analyze.html',juned)

	if(counter=="on"):
		count=0
		for char in djtext:
			count=count+1
		juned={'purpose':'Character Counter','analyzed_text':count}
		#Analyzed the text
		return render(request,'analyze.html',juned)
	if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on" and counter!="on"):
		return HttpResponse("Please select an operation")

	return render(request,'analyze.html',juned)
