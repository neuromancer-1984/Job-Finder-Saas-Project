from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import login


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user =  form.save()
            login(request,user)
            return redirect('/')
        
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})