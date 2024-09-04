
from rest_framework import viewsets, serializers, status, generics
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .authentication import SessionTokenAuthentication

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]
    authentication_classes = [SessionTokenAuthentication]

    def get_queryset(self):
        print(self.request.user)
        if self.request.user.is_anonymous:
            return Task.objects.none()
        return self.queryset.filter(user=self.request.user)
    
    def update(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        print('update user', request.user)
        print('update data', request.data)
        return super().update(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        print('create user', request.user)
        print('create data', request.data)
        # convert date from 2024-09-03 to 2024-09-03T00:00:00Z
        request.data['dueDate'] += 'T00:00:00Z'
        request.data['user'] = request.user.id
        request.data['userId'] = request.user.id
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)