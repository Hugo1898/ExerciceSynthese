from django.urls import path
from . import views

urlpatterns = [
    path('albums/', views.voir_albums, name='albums'),
    path('tracks/<int:album_id>', views.voir_tracks, name='tracks'),
]