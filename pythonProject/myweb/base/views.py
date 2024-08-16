from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Eshkhi, User, Style
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm, UserForm
from django.contrib import messages
=======
>>>>>>> origin/main

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""

    # clothes = Eshkhi.objects.all()
    clothes = Eshkhi.objects.filter(Q(color__icontains=q) | Q(description__icontains=q) | Q(style__name__icontains=q) )
    clothes = list(set(clothes))
    styles = Style.objects.all()
    # print((clothes[0].users.all()))
    heading = "ESHKHI"
    context = {"clothes": clothes, "heading": heading, "styles": styles}
    return render(request, 'base/home.html', context)



def about(request):
    return render(request, 'base/about.html')


def contact(request):
    return render(request, 'base/contact.html')


def profile(request, pk):
    user = User.objects.get(id=int(pk))
    q = request.GET.get('q') if request.GET.get('q') != None else ""

    clothes = user.clothes.filter(Q(color__icontains=q) | Q(description__icontains=q) | Q(style__name__icontains=q))
    clothes = list(set(clothes))

    heading = "My favourites"
    context = {'clothes': clothes, "user": user, "heading": heading}
    return render(request, 'base/profile.html', context)


<<<<<<< HEAD
@login_required(login_url='login')
=======
>>>>>>> origin/main
def adding(request, id):
    clothe = Eshkhi.objects.get(id=id)
    user = request.user
    user.clothes.add(clothe)
    return redirect('profile', user.id)


<<<<<<< HEAD
@login_required(login_url='login')
=======
>>>>>>> origin/main
def delete(request, id):
    clothe = Eshkhi.objects.get(id=id)
    if request.method == "POST":
        request.user.clothes.remove(clothe)
        return redirect('profile', request.user.id)
    return render(request, 'base/delete.html', {'clothe': clothe})


def login_page(request):
<<<<<<< HEAD
=======
    page = 'login'

>>>>>>> origin/main
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password').lower()

        try:
            user = User.objects.get(username=username)
        except:
<<<<<<< HEAD
            messages.error(request, "Username doesn't exist! ")
=======
            pass
>>>>>>> origin/main

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
<<<<<<< HEAD
            messages.error(request, "Username or password is incorrect! ")

    return render(request, 'base/login.html')
=======
            pass

    context = {'page': page}
    return render(request, 'base/login_register.html', context)
>>>>>>> origin/main


def logaut_user(request):
    logout(request)
    return redirect('home')


def register_page(request):
<<<<<<< HEAD
    form = MyUserCreationForm()

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/register.html', context)


def delete_clothe(request, id):
    clothe = Eshkhi.objects.get(id=id)
    return render(request, 'base/delete.html', {'clothe': clothe})


@login_required(login_url='login')
def update_user(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', user.id)

    return render(request, 'base/update_user.html', {'form': form})
=======
    context = {}
    return render(request, 'base/login_register.html', context)

>>>>>>> origin/main
