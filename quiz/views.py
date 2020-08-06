from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAdminUser


class QuizViewSet(viewsets.ModelViewSet):

    serializer_class = QuizSerializers

    def get_queryset(self):
        if self.action == 'list':
            if not self.request.user.is_superuser:
                return Quiz.objects.filter(is_active=True)
        return Quiz.objects.all()

    def get_permissions(self):
        if self.action not in ['list', 'retrieve']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]
