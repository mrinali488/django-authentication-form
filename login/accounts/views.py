from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.


def index_view(request):
    return render(request, 'index.html')


class signup_view(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    success_message = "%(username)s was Logged in successfully"






"""
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()  # blank form
    return render(request, 'registration/signup.html', {'form': form})
"""

"""

def signup_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = RegisterForm()  # blank form
    return render(request, 'registration/signup.html', {'form': form})
    """


@login_required()
def profile_view(request):
    return render(request, 'profile.html')

