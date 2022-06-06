from django.urls import path
from . import views

urlpatterns = [

    path('home/',views.home,name='tracker-home'),
    path('task/<str:username>', views.UserTasks.as_view() ,name='user-task'),
    path('card/new/', views.CardCreateView.as_view() ,name='card-create'),
    path('card/<int:pk>/', views.CardDetailView.as_view() ,name='card-detail'),


]