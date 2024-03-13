from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(),name='home'),
    path("inscription/", views.Inscription, name="inscription"),
    path("connection/", views.connection, name="connection"),
    path("deconnection/", views.deconnection, name="deconnection"),
    path("offre_emploi/<int:pk>/", views.offre_emploi, name="offre_emploi"),
    path("offre_emploi/<int:pk>/candidature/", views.candidature, name="candidature"),
    path("offre_emploi/<int:pk>/candidature/success", views.SuccessView.as_view(),name='success'),
    path("annonce/", views.annonce, name="annonce")
]