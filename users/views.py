from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import registrationForm

class register(View):
	def get(self, request, *args, **kwargs):
		form = registrationForm()
		return render(request, 'users/auth/register.html', {'form':form})

	def post(self, request, *args, **kwargs):
		form = registrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
		else:
			return redirect('register')

