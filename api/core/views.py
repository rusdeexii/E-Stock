# core/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello from core app!")
