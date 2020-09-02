from book import views

from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'book', views.BookViewSet)
router.register(r'author', views.AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
