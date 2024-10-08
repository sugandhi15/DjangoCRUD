from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("addNote",views.add,name="add"),
    path("viewNotes",views.viewnt,name="view"),
    path("viewNote/<int:pk>",views.viewSpecificNote,name="viewSpecificNote"),
    path("editNote/<int:param>",views.edit,name="edit"),
    path("delete/<int:param>",views.delete,name="delete"),
    path("deleteall",views.deleteall,name="deleteall")
]
