from django.urls import path
from . import views

urlpatterns = [
    path('person/<int:question_id>/', views.detail, name='detail'),
    path('person/', views.index, name='index'),
    path('json/encode', views.jsonEncode, name='json.encode'),
    path('json/decode', views.jsonDecode, name='json.decode'),
    path('api/person', views.PersonList.as_view(), name='api.person'),
]