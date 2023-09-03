"""
URL configuration for pollsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from polls import (
    views,
)  # Asegúrate de importar el módulo de vistas de la aplicación "polls"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("polls/", include("polls.urls")),  # Incluye las URLs de la aplicación "polls"
    path(
        "", views.question_list, name="question_list"
    ),  # Asigna la vista question_list
]
