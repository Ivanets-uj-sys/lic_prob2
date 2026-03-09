from django.http import HttpRespone

def index(request):
	return HttpResponse("Hello, world!")
