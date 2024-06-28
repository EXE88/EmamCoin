from . import views
from django.urls import path

urlpatterns = [
    path('register/',views.UserRegisterPageView.as_view(),name="user_register_page"),
]