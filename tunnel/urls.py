from . import views
from django.urls import path

urlpatterns = [
    path('addcoin/<str:username>/<int:value>/',views.AddCoinTunnelView,name='user_add_coin_tunnel'),
]