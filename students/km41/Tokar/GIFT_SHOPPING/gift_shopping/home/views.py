from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from gifts.models import Bucket
from .forms import SignUpForm


def home(request):
    template_name = 'home.html'

    return render(request, template_name)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            Bucket.objects.create(user_id=request.user.id, name='My Gift Bucket')

            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
