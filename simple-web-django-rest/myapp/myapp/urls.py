from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

urlpatterns = [
    path('main/', include('myapp.app.main.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns +=[
path('main/api/auth', include('rest_framework.urls', namespace = 'rest_framework')),
]