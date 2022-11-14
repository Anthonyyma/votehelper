from django.shortcuts import render


def index(request):
    context = {"name":"John"}
    return render(request, "survey.html", context)
