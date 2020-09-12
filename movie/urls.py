from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('actor/', views.actor_index, name='actor list'),
    path('filmdetail/<int:film_num>/', views.film, name='film'),
    path('actordetail/<int:actor_num>/', views.actor, name='actor'),
    path('search/', views.search_place, name='search'),
    path('search0/', views.search, name='search')
]
