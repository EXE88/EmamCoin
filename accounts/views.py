from django.shortcuts import render , redirect
from . import forms
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login 
from django.contrib import messages

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
            new_user = User.objects.create_user(username=cd['username'])
            login(request , new_user)
            return redirect('mine_coin_page')
        messages.error(request , 'user already exists' , 'danger')
        return render(request , self.template_name , {"form":form})
