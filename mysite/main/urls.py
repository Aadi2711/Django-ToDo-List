from django.urls import path

from . import views

urlpatterns=[
    path("<int:id>",views.index, name="index"),
    path("", views.home, name="home"),
    # path("v1/",views.v1,name="index"),
    path("create/", views.create, name="create")
]