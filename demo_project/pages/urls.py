from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path("join", views.join, name="join"),
    #path('join/', views.Join.as_view(), name='join'),
    path("signin", views.signin, name="signin"),
]
