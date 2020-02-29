
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
from party.models import Party
from party.serializer import PartySerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('Party.home')
    else:
        form = UserCreationForm()
return render(request, 'accounts/signup.html'.{'form'.form})

def 
