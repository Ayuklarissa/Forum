from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('groupe/<int:pk>/question', views.question, name='question'),
    path('groupe/', views.groupe,name='groupe'),
    path('groupe/<int:pk>/question/<int:pk_question>/repondre', views.repondre, name='repondre'),
    path('question/<int:pk_question>/repondre', views.respond_to_question, name='respond_to_question'),
    path("signup/", views.SignUpView, name="signup"),
    path("groupe/<int:pk>/liste", views.liste, name="liste"),
    path("groupe/<int:pk>/not_member", views.not_member, name="not_member"),
    path("groupe/<int:pk>/liste/<int:pk_membre>/not_member", views.add_member, name='add_member')
    # path('groupe/<int:pk>/liste/<int:pk_membre>/not_member', views.add_member, name='not_member'),

]

