"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import index_view, note_create_view, note_view, note_update_view, note_delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('note/<int:pk>/', note_view, name='note_view'),
    path('notes/add/', note_create_view, name='note_create'),
    path('note/<int:pk>/update/', note_update_view, name='note_update'),
    path('note/<int:pk>/delete/', note_delete_view, name='note_delete'),

]