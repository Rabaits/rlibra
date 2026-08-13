from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('creat_note', views.index_create, name='creat_note'),
    path('note/<int:note_id>/', views.note_visibel, name='notes')
]
