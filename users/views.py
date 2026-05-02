from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        village = request.POST.get('village', '')
        district = request.POST.get('district', '')
        state = request.POST.get('state', 'Uttarakhand')
        
        if password != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'users/register.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return render(request, 'users/register.html')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        Profile.objects.create(user=user, village=village, district=district, state=state)
        login(request, user)
        messages.success(request, f'Welcome to Mountain Coders, {username}!')
        return redirect('home')
    return render(request, 'users/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect(request.GET.get('next', 'home'))
        messages.error(request, 'Invalid username or password.')
    return render(request, 'users/login.html')

def user_logout(request):
    logout(request)
    messages.info(request, 'Logged out successfully.')
    return redirect('home')

@login_required
def profile(request):
    profile_obj, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.email = request.POST.get('email', '')
        request.user.save()
        profile_obj.bio = request.POST.get('bio', '')
        profile_obj.village = request.POST.get('village', '')
        profile_obj.district = request.POST.get('district', '')
        profile_obj.state = request.POST.get('state', 'Uttarakhand')
        profile_obj.phone = request.POST.get('phone', '')
        profile_obj.save()
        messages.success(request, 'Profile updated!')
        return redirect('profile')
    return render(request, 'users/profile.html', {'profile': profile_obj})
