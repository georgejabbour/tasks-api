from rest_framework import viewsets
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