from .serializers import constructionSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from .models import construction , organization ,building


class UserViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = construction.objects.all()
        serializer = constructionSerializers(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = construction.objects.all()
        serializer = constructionSerializers()
        return Response(serializer.data)

class constructionListView(viewsets.ViewSet):

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass