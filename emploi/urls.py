from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(),name='home'),
    path("inscription/", views.InscriptionView.as_view(), name="inscription"),
    path("connection/", views.ConnectionFormView.as_view(), name="connection"),
    path("deconnection/", views.DeconnectionView.as_view(), name="deconnection"),
    path("offre_emploi/<int:pk>/", views.OffreEmploiDetailView.as_view(), name="offre_emploi"),
    path("offre_emploi/<int:pk>/candidature/", views.CandidatureCreateView.as_view(), name="candidature"),
    path("offre_emploi/<int:pk>/candidature/success", views.SuccessView.as_view(),name='success'),
    path("annonce/", views.AnnonceFormView.as_view(), name="annonce")
]