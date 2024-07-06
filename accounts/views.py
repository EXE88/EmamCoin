from django.shortcuts import render , redirect
from . import forms
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login 
from django.contrib import messages
import requests

class UserRegisterPageView(View):
    form_class = forms.UserRegisterPageForm
    template_name = "accounts/UserRegisterPage.html"

    def get(self,request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            check_user_exists = requests.post(f'http://127.0.0.1:5000/user/create/{cd['username']}').status_code
            if check_user_exists == 200:
                new_user = User.objects.create_user(username=cd['username'])
                login(request , new_user)
                return redirect('mine_coin_page')
            messages.error(request , 'user already exists' , 'danger')
            return render(request , self.template_name , {"form":form})
        messages.error(request , 'user already exists' , 'danger')
        return render(request , self.template_name , {"form":form})
