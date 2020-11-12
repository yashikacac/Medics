from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
#from .model import Login
# Create your views here.

# def details(request):
#     if request.method is 'POST':
#         user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#     return (render, )
def details(request):
	if request.method == 'POST':
		tempForm = UserCreationForm(request.POST)
		tempForm.save()
		#return HttpResponse("Details saved successfully")
		return redirect('login')

	else:
		form = UserCreationForm()
	return render(request, 'app1/details.html', {'form': form})

# def login_request(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {username}")
#                 return redirect('/')
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Invalid username or password.")
#     form = AuthenticationForm()
#     return render(request = request,template_name = "app1/login.html",context={"form":form})

# def logout_request(request):
# 	logout(request)
# 	messages.info(request, "Logged out successfully!")
# 	return redirect("main:homepage")
