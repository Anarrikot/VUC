from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly, UserPermission
from .utils import SolderAPIPagination
from .models import Solder, Title
from .serializers import SolderSerializer, SolderDetailSerializer
from rest_framework import viewsets

class SolderViewSet(viewsets.ModelViewSet):
    pagination_class = SolderAPIPagination
    queryset = Solder.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SolderDetailSerializer
        return SolderSerializer

    @action(methods=['get'], detail=True)
    def title(self, request, pk=None):
        title = Title.objects.filter(pk=pk).first()
        if title:
            return Response({'category': f'{title.name}'})
        else:
            return Response({'category': 'Категория не найдена'})

    @action(methods=['get'], detail=True)
    def title(self, request, pk=None):
        title = Title.objects.get(pk=pk)
        return Response({'title': f'{title.name}'})