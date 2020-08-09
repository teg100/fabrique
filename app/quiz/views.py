from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import *


class QuizViewSet(viewsets.ModelViewSet):
    """
            CRUD operations for quiz
    """
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
    """
        CRUD operations for question
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]


class ResponseCreateView(viewsets.ModelViewSet):
    """
            Create response
        """

    serializer_class = ResponseSerializer


class ResponseUserList(ListAPIView):
    """
        List responses for current user
    """
    serializer_class = ResponseSerializer

    def get_queryset(self):
        queryset = Response.objects.filter(uid=self.kwargs['uid'])
        return queryset
