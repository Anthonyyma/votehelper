from django.urls import path

from . import views

app_name = "votehelperapp"
urlpatterns = [
    path('', views.index, name='index'),
]