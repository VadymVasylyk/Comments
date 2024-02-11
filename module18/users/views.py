from django.shortcuts import render, redirect
from .forms import UserRegForm


def register(request):
    if request.method == "POST":
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegForm()
    return render(request, 'users/register.html', {'form': form})


