from django.shortcuts import render

#home
def home(request):
	context = {}
	return render(request, 'main/home/home.html', context)
