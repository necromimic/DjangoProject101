from django.urls import path
from DBlog.views import about, contact, index, persons
urlpatterns = [
    path('', index),
    path('about/', about),
    path('contact/', contact),
    path('persons/', persons)
]