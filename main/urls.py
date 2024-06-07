from . import views
from django.urls import path

urlpatterns = [
    path('',views.MineCoinPage.as_view(),name='mine_coin_page'),
]