from django.urls import path

from . import views

urlpatterns = [
   path("terms_list/", views.terms_list, name="terms_list"),
   path("consulta-termo/", views.consulta_termo, name="consulta-termo"),
   path("", views.index, name="index")
]