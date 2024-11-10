from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# path takes the arguments of (url, view function, name)
# e.g. a url like '/login' can be accessed from http://127.0.0.1:8000/login
# e.g. the name is what you use to link to the page in our html files
app_name = "railway"
urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home")

]
urlpatterns += staticfiles_urlpatterns()