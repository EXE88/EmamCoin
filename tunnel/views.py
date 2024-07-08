import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def AddCoinTunnelView(request,username,value):
    response = requests.post(f"http://127.0.0.1:5000/user/coin/add/{username}/{value}")
    return JsonResponse({"response":response.json()})