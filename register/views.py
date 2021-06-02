from django.shortcuts import render,redirect
from register import forms as f

# Create your views here.
def register(response):
    if response.method == "POST":
        form = f.RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
	       form = f.RegisterForm()
    return render(response,'register.html',{"form":form})
