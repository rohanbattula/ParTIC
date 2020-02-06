from django.shortcuts import render
from django.http import JsonResponse
from models import Party
from serializer import PartySerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
