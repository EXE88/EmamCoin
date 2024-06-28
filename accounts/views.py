from django.shortcuts import render
from . import forms
from django.views import View

class UserRegisterPageView(View):
    form_class = forms.UserRegisterPageForm
    template_name = "accounts/UserRegisterPage.html"

    def get(self,request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
