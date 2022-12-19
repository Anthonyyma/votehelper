from django.urls import path

from . import views

urlpatterns = [
    path('', views.stats, name='stats'),
    # path('create/', views.addVoter, name='create'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.register, name='register'),
    path('survey/', views.survey, name='survey'),
    path('list/', views.VoterList.as_view(), name='voterlist'),
    path('add/', views.import_csv, name='import_csv'),
    path('assign/', views.add_user_to_group, name='add_user_to_group'),
]