from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("addNote",views.add,name="add"),
    path("viewNotes",views.viewnt,name="view"),
    path("delete/<int:param>",views.delete,name="delete")
]
