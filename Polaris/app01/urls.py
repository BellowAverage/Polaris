from django.urls import path
from . import views

urlpatterns = [
    path('function/get_suggestion/<str:text>/', views.get_suggestion, name='function_get_suggestion'),
    path('example/', views.example, name='example'),
    path('example/process_json/', views.process_json, name='process_json'),
    path('example/get_suggestion/<str:text>/', views.get_suggestion, name='get_suggestion'),
    path('polaris/template/', views.template, name='template'),
    path('polaris/', views.polaris, name='polairs'),
    path('polaris/login/', views.login, name='login'),
    path('polaris/dashboard/<str:uid>/', views.dashboard, name='dashboard'),
    path('polaris/write_note/<str:uid>/', views.write_note, name='write_note'),
    path('polaris/my_space/<str:uid>/', views.my_space, name='my_space'),

]