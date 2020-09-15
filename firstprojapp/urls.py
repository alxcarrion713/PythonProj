from django.urls import path
from.import views

urlpatterns = [
    path("",views.index),
    path("new",views.new),
    path("<int:my_val>",views.show),
    path("<int:my_val>/edit", views.edit),
    path("destroy",views.destroy),
]