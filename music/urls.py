from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artists/', views.Artistlist),
    path('artists/<str:pk>/', views.Artistdetail),
    path('artists/<str:pk>/albums/', views.Artistalbums),
    path('artists/<str:pk>/tracks/', views.Artisttracks),
    path('albums/', views.Albumlist),
    path('albums/<str:pk>/', views.Albumdetail),
    path('albums/<str:pk>/tracks/', views.Albumtracks),
    path('tracks/', views.Tracklist),
    path('tracks/<str:pk>/', views.Trackdetail),
]

