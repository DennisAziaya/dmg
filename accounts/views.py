# accounts/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_view(request):
    if request.user.is_authenticated:
        # Redirect to the dashboard if the user is already authenticated
        return redirect('accounts:dashboard')

    if request.method == 'POST':
        workspace_id = request.POST.get('workspace_id')
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        # Check if all fields are provided
        if workspace_id and username_or_email and password:
            # Try to authenticate the user
            user = authenticate(request, username=username_or_email, password=password)

            if user is not None and user.workspace_id == workspace_id:
                login(request, user)
                # Redirect to a success page or home page
                return redirect('accounts:dashboard')
            else:
                messages.error(request, 'Invalid login credentials')
        else:
            messages.error(request, 'Please provide all login credentials')

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    # Redirect to a success page or home page
    return redirect('accounts:login')


@login_required(login_url='accounts:login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')



