from django.shortcuts import render
from .forms import VoterForm
from .models import Voter
from django.views.generic import ListView

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
        else:
            print(form.errors)

    context = {'form': form, 'id':voterId, 'voter':voter}
    return render(request, "survey.html", context)
