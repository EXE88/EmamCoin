from . import views
from django.urls import path

urlpatterns = [
    path('',views.MineCoinPageView.as_view(),name='mine_coin_page'),
]