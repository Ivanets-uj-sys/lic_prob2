from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world! Moja pierwsza strona za pomocą django")
