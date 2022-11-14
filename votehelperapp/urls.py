from django.urls import path

from . import views

urlpatterns = [
    path('', views.survey, name='survey'),
    path('list/', views.VoterList.as_view(), name='voterlist'),
]