from django.contrib import admin
from django.urls import path
from Discussion.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('addInGroup/', addInGroup,name='addInGroup'),
    path('addInMessage/',addInMessage,name='addInMessage'),
    path('addInMember/',addInMember,name='addInMember'),
]