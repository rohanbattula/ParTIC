'''
from django.shortcuts import render
from django.http import JsonResponse
from models import Party
from serializer import PartySerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    rest_list = Party.objects.order_by('-pub_date')
    context = {'rest_list': rest_list}
    return render(request, 'index/index.html', context)


# Rest api end point
def get_rest_list(request):
    """
    Returns Json list of all restaurants
    """
    if request.method == "GET":
        rest_list = Party.objects.order_by('-pub_date')
        serializer = PartySerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)
'''

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the party index.")