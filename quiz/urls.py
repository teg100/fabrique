from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'quizes', QuizViewSet, basename='quiz')
router.register('questions', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls))
]