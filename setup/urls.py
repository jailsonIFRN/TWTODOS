
from django.contrib import admin
from django.urls import path

from todos.views import home

# todas a rotas existentes para ser executadas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]

