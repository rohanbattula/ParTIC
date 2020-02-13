
from django.shortcuts import render
from django.http import JsonResponse
from party.models import Party
from party.serializer import PartySerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    rest_list = Party.objects.order_by('-dateTime')
    context = {'rest_list': rest_list}
    return render(request, 'party/index.html', context)


# Rest api end point
def get_rest_list(request):
    """
    Returns Json list of all restaurants
    """
    if request.method == "GET":
        rest_list = Party.objects.order_by('-dateTime')
        serializer = PartySerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)
