from django.shortcuts import render, redirect
from .forms import VoterForm, CreateForm
from .models import Voter
from django.views.generic import ListView
import csv

class VoterList(ListView):
    template_name = "voterlist.html"
    model = Voter

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
    yes = Voter.objects.filter(decision=1).count
    no = Voter.objects.filter(decision=2).count

    context = {'yes':yes, 'no':no}
    return render(request, "stats.html", context)

def addVoter(request):
    form = CreateForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        form = CreateForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            return redirect("/list")
        else:
            print(form.errors)

    context = {'form': form}
    return render(request, "addvoter.html", context)

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
            for line in lines:
                fields = line.split(",")
                voter = Voter(name=fields[0], address=fields[1])
                voter.save()

        except Exception as e:
            print(e)
    return redirect("/list")
