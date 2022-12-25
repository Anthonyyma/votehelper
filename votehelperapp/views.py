from django.shortcuts import render, redirect
from .forms import VoterForm
from .models import Voter
from django.views.generic import ListView
import csv
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User


class VoterList(ListView):
    template_name = "voterlist.html"
    model = Voter

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('voterlist')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('stats')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def survey(request):
    form = VoterForm(request.POST or None, request.FILES or None)
    voterId = request.GET.get('id')  
    if voterId != None:
        voter = Voter.objects.get(id=voterId)
        form = VoterForm(instance=voter)
    if request.method == "POST":
        if voterId != None:
            form = VoterForm(request.POST, instance=voter)
        else:
            form = VoterForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            return redirect("/list")
        else:
            print(form.errors)

    a = Voter.objects.filter(decision=1).count

    context = {'form': form, 'id':voterId, 'voter':voter}
    return render(request, "survey.html", context)

def stats(request):
    # if request.user.is_superuser:
    #     return redirect('assign')

    yes = Voter.objects.filter(decision=1).count
    no = Voter.objects.filter(decision=2).count

    context = {'yes':yes, 'no':no}
    return render(request, "stats.html", context)

# def assign(request):
#     User = get_user_model()
#     users = User.objects.all()
#     nei = Neighbourhood.objects.all()
#     groups = Group.objects.all()

#     context = {'users':users, 'nei':nei, 'groups':groups}
#     return render(request, "assign.html", context)

def assign(request):
    user_pk = request.POST.get('user')
    group_name = request.POST.get('group')
    groups = Group.objects.all()
    User = get_user_model()
    users = User.objects.all()

    if request.method == 'POST':
        # Get the user and group objects
        user = User.objects.get(pk=user_pk)
        group = Group.objects.get(name=group_name)

        # Remove the user from their current group (if they are in one)
        if user.groups:
            user.groups.clear()

        # Add the user to the group
        group.user_set.add(user)

    context = {'users':users, 'groups':groups}
    return render(request, "assign.html", context)

def assignIndividual(request):
    user_pk = request.POST.get('user')
    voter_names = request.POST.getlist('options')
    voters = Voter.objects.all()
    User = get_user_model()
    users = User.objects.all()

    if request.method == 'POST':
        # Get the user and group objects
        if user_pk.isdigit():
            user = User.objects.get(pk=user_pk)
            for voter_name in voter_names:
                voter = Voter.objects.get(name=voter_name)
                voter.assignedEmp = user.username
                voter.save()

    context = {'users':users, 'voters':voters}
    return render(request, "assignIndividual.html", context)

# @login_required
# @require_POST
def import_csv(request):
    if request.method == 'POST':
        try:
            csv_file = request.FILES['csv_file']
            data = csv_file.read().decode("utf-8")
            if not csv_file.name.endswith(".csv"):
                return redirect("/list")
            
            lines = data.split("\n")
            lines.pop(0)
            for line in lines:
                if not line:
                    continue

                reader = csv.reader([line])
                fields = next(reader)
                nei = fields[2].strip()

                # create the group
                group = Group.objects.filter(name=nei)

                if not group:
                    group = Group.objects.create(name=nei)
                voter = Voter(name=fields[0], address=fields[1], neighbourhood=nei)
                voter.save()

        except Exception as e:
            print(e)
    return redirect("/list")
