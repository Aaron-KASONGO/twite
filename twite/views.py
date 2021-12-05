from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .forms import SignUpForm, PostForm, UpdateProfileForm, UpdateUserForm

# Create your views here.
@login_required
def home(request):
    return render(request, 'twite/home.html')


def  signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
        else:
            return render(request, 'twite/sign_up.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'twite/sign_up.html', {'form': form})
    
@login_required
def to_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(reverse('home'))
        else:
            return render(request, 'twite/create_post.html', {'form':form})
    else:
        form = PostForm()
        return render(request, 'twite/create_post.html', {'form':form})


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST,request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect(reverse('home'))
        else:
            return render(request, 'twite/update_profile.html', {'user_form':user_form, 'profile_form':profile_form})
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
        return render(request, 'twite/update_profile.html', {'user_form':user_form, 'profile_form':profile_form})


class Login(views.LoginView):
    template_name = 'twite/login.html'


class Logout(views.LogoutView):
    next_page = reverse_lazy('home')