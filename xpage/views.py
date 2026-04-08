from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
	return render(request, 'xpage/index.html',{})


def about(request):
	return render(request, 'xpage/about.html',{'name':'Enisi the Owner of the page'})

def allmovies(request):
	context = {
	'movies':['Stugo','postimi 2','postimi 3','postimi 4']
	}
	return render(request, 'xpage/movies.html',context)

#this called dynamic url
def select(request,name):
	return HttpResponse(f'Hello {name}')

def adding(request, num1,num2):
	return HttpResponse(f'Total is: {num1+num2}')