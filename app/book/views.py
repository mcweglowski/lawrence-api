from book.serializers import AuthorSerializer, BookSerializer

from core.models import Author, Book

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title', None)
        if title is not None:
            self.queryset = self.queryset.filter(title=title)
        return self.queryset


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello World!"})
