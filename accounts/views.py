from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .forms import AccountAuthenticationForm

# Create your views here.

def logout_view(request):
	logout(request)
	return redirect('/')


def login_view(request):

	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect("/")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect("/add-bid/")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	# print(form)
	return render(request, "accounts/login.html", context)