from django.contrib import admin
from django.urls import path

from todos.views import todo_list



# todas a rotas existentes para ser executadas - vem do "setup > urls.py"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", todo_list),

]
