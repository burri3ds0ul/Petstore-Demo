from django.urls import path
from .views import PostPetListView, PostPetDetailView, PostPetCreateView, PostPetUpdateView, PostPetDeleteView, UserPostPetListView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/<str:username>', UserPostPetListView.as_view(), name='user-post'),
    path('about/', PostPetListView.as_view(), name='about'),
    path('about/<int:pk>/', PostPetDetailView.as_view(), name='post-detail'),
    path('about/new/', PostPetCreateView.as_view(), name='post-create'),
    path('about/<int:pk>/update/', PostPetUpdateView.as_view(), name='post-update'),
    path('about/<int:pk>/delete/', PostPetDeleteView.as_view(), name='post-delete'),
    path('contact/', views.contact, name='contact'),
]

