from django.urls import path
from .views import import homePageView

urlpatterns = [
    path("", homePageView, name= "home"),
]