from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_item, name='add_item'),
    path('complete/<int:item_id>/', views.complete_item, name='complete_item'),

]
