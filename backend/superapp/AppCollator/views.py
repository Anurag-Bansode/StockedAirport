from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .stock import stocklist
import requests,datetime


# Create your views here.
def index(request):
    return HttpResponse("TestResponse")

def get_api_data(request):
   return stocklist()

def get_aviation_data(request):
    url = "https://aviationweather.gov/api/data/airport?ids=KORD,KBOS,KJFK&format=json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return JsonResponse({'status': 'success', 'data': data}, status=200)
        else:
            return JsonResponse({'status': 'error', 'message': 'Failed to fetch data.'}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

def get_flight_data(request):
    airport_code = request.GET.get('airport')
    start_of_day = int(datetime.datetime.combine(datetime.date.today(), datetime.datetime.min.time()).timestamp())
    end_of_day = int(datetime.datetime.now().timestamp())
    url = f"https://opensky-network.org/api/flights/departure?airport={airport_code}&begin={start_of_day}&end={end_of_day}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return JsonResponse({'status': 'success', 'data': data}, status=200)
        else:
            return JsonResponse({'status': 'error', 'message': 'Failed to fetch data.'}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

