from django import forms
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('formulario/', views.formulario, name='formulario'),


    path('data/', views.load_post_data_view, name='posts-data'),
    path('index/', views.post_list_and_create, name="indextwo"),
    path('hello-world/', views.hello_world_view, name='hello-world'),

    # Testando chartjs
    path('chart/', views.chartjs, name="chartjs"),
]