from django.urls import path

from . import views

urlpatterns = [
    path('stats/', views.stats, name='stats'),
    # path('create/', views.addVoter, name='create'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.register, name='register'),
    path('survey/', views.survey, name='survey'),
    path('', views.VoterList.as_view(), name='voterlist'),
    path('add/', views.import_csv, name='import_csv'),
    path('assign/', views.assign, name='assign'),
    path('addvoter/', views.addVoter, name='addvoter'),
    path('assignindividual/', views.assignIndividual, name='assignindividual'),
    path('export/', views.export, name='export'),
]