
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_tasks, name='homepage'),
    path('task/', include('task.urls')),
    path('category/', include('category.urls')),
]
