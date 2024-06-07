from django.shortcuts import render
from django.views import View

class MineCoinPage(View):
    template_name = "main/MineCoinPage.html"
    def get(self,request):
        return render(request , self.template_name)