
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse
from party.models import Party
from party.serializer import PartySerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import PartyForm
from .forms import SignUpForm

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
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.username = form.cleaned_data.get('username')
            user.profile.email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            string msg = email.message_from_string(data[0][1])
            string addr = email.utils.parseaddr(msg['From'])[1]
            domain = addr.split('@')[1]
            if domain == "ucla.edu" || domain == "g.ucla.edu":
                messages.success(request, f'Registration successful!')
                login(request, user)
                return redirect('/party/view.html')
            else:
                messages.self.fail('Registration unsuccessful')
    else:
        form = SignUpForm()
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

def login(request, user):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})

def logout_view(request):
    logout(request)
    return redirect('/login.html')
