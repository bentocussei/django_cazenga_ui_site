"""
URL configuration for django_tailwind_alpine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.shortcuts import render

from core.views import index, demo, components_list, component_detail, icons_page

def spa_test(request):
    """View para testar o sistema SPA"""
    return render(request, "spa-test.html")

urlpatterns = [
    path("", index, name="index"),
    path("demo/", demo, name="demo"),
    path("components/", components_list, name="components_list"),
    path("components/<slug:component_name>/", component_detail, name="component_detail"),
    path("icons/", icons_page, name="icons_page"),
    path("spa-test/", spa_test, name="spa_test"),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]