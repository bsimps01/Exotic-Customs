from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import UserCreateForm
from django.contrib import messages
from accounts.models import Profile
from django.views.generic.list import ListView
from django.contrib.auth.models import User



class SignUpView(CreateView):
  form_class = UserCreateForm
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'

class Foundation(CreateView):
  def get(self, request):
      return render(request, "base.html")

class Homepage(CreateView):
    def get(self, request):
        return render(request, "accounts/home.html")

def index(request):
    return HttpResponse("Hello, world. You're at the best website here")

def update_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('list-rides-page')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/profile.html', {
        'profile_form': profile_form
    })

class ProfilesListView(ListView):

    def get(self, request):
        cars = User.objects.filter(profile__is_passenger=False)
        return render(request, 'accounts/profile_list.html', {'profiles': cars})

class Ferrari(CreateView):

    def get(self, request):
        cars = User.objects.filter
        return render(request, 'accounts/ferrari.html', {'ferrari': cars})

class Bugatti(CreateView):

    def get(self, request):
        cars = User.objects.filter
        return render(request, 'accounts/bugatti.html', {'bugatti': cars})

class McLaren(CreateView):

    def get(self, request):
        cars = User.objects.filter
        return render(request, 'accounts/mclaren.html', {'mclaren': cars})

class Lamborghini(CreateView):

    def get(self, request):
        cars = User.objects.filter
        return render(request, 'accounts/lamborghini.html', {'lamborghini': cars})

def login_view_profile(request):
        user = request.user
        args = {'user': user}
        return render(request, 'accounts/account.html', args)

class ConfirmPage(CreateView):

    def get(self, request):
        return render(request, 'accounts/request_confirm.html')
# Create your views here.
