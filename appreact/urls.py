from django.urls import path
from .views import index, index_react
urlpatterns = [
    path('', index, name='index'),
    path('react/', index_react, name='indexreact')
]


