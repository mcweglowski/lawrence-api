from book import views

from django.conf.urls import url
from django.urls import include, path

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'authors', views.AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url('', views.hello_world, name='hello-world'),
]
