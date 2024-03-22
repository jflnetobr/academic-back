from dataclasses import dataclass

from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.views import Response
from rest_framework.viewsets import ModelViewSet

from services.models import Notification
from services.serializers import NotificationSerializer

@dataclass()
class NotificationModelViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    
    def __init__(self, *args, **kwargs):
        self.suffix = kwargs.pop('suffix', None)
        super().__init__(*args, **kwargs)

    def list(self, request):
        forms = Notification.objects.all()
        serializer = NotificationSerializer(forms, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def create(self, request):
        
        # Implementar função que gerencie a criação de um notification
        # Implementar permissões para criação de notification
 
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
 
 
    def partial_update(self, request, pk=None):
        notification = Notification.objects.get(pk=pk)
        notification.co_status = request.data.get('co_status')
        notification.save()
        serializer = NotificationSerializer(notification)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def delete(self, request):

        pk = request.data.get('co_notification')

        # Implementar função que gerencie a exclusão de um notification
        # Implementar permissões para exclusão de notification

        form = Notification.objects.get(pk=pk)
        form.delete()

        return Response(NotificationSerializer(form).data, status=HTTP_200_OK)