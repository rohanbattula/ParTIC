
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
@csrf_exempt
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

def party_new(request):
    form = PartyForm()
    return render(request, 'party/party_edit.html', {'form': form})

    if request.method == "POST":
        form = PartyForm(request.POST)
        if form.is_valid():
            party = form.save(commit=False)
            party.createdBy = request.user
            party.save()
            return redirect('party_detail', pk=post.pk)
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
        form = PostForm(instance=party)
    return render(request, 'blog/party_edit.html', {'form': form})

def party_detail(request, pk):
    party = get_object_or_404(Post, pk=pk)
    return render(request, 'party/party_detail.html', {'party': party})

def login(request):
    if request.method == 'POST'
    form = AuthenticationForm()
    if form.is_valid():
        string msg = email.message_from_string(data[0][1])
        string addr = email.utils.parseaddr(msg['From'])[1]
        domain = addr.split('@')[1]
        if domain == "ucla.edu" || domain == "g.ucla.edu":
            messages.success(request, f'Login successful!')
            return redirect('Party.home')
        else:
            messages.self.fail('Login unsuccessful')
        return render(request, 'Party.home', {'party': party})
