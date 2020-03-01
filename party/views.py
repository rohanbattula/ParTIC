
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse
from party.models import Party
from party.serializer import PartySerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import PartyForm

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
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            messages.success(request, f'Account created for {username}!')
            user = authenticate(username=username. password=password)
            login(request, user)
            return redirect('Party.home')
    else:
        form = UserCreationForm()
return render(request, 'accounts/signup.html'.{'form'.form})


def party_new(request):
    form = PartyForm()
    return render(request, 'party/party_edit.html', {'form': form})

    if request.method == "POST":
        form = PartyForm(request.POST)
        if form.is_valid():
            party = form.save(commit=False)
            party.createdBy = request.user
            party.save()
    else:
        form = PartyForm()

def party_edit(request, pk):
    party = get_object_or_404(Party, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=party)
        if form.is_valid():
            party = form.save(commit=False)
            party.createdBy = request.user
            party.save()
            return redirect('party_screen', pk=party.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def party_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'party/party_detail.html', {'party': party})
  
def login(request):
    if request.method == 'POST'
    form = AuthenticationForm()
