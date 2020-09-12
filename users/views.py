from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .forms import RegisterForm, UpdateProfileForm, UpdateProfilePicForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created. You can login now!')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form':form})




@login_required
def profile(request):
    if request.method == 'POST':
        user_from = UpdateProfileForm(request.POST, instance=request.user)
        pic_form = UpdateProfilePicForm(request.POST, 
                                        request.FILES, 
                                        instance=request.user.profile)

        if user_from.is_valid() and pic_form.is_valid():
            user_from.save()
            pic_form.save()
            messages.success(request, f'Account Updated!')
            return redirect('profile')
    else:
        user_from = UpdateProfileForm(instance=request.user)
        pic_form = UpdateProfilePicForm(instance=request.user.profile)

    context = {
        'user_form': user_from,
        'pic_form': pic_form
    }

    return render(request, 'users/profile.html', context)

