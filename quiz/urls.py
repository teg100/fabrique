from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'quizes', QuizViewSet, basename='quiz')
router.register('questions', QuestionViewSet)
response_create = ResponseCreateView.as_view({'post': 'create'})
# router.register('responses', ResponseCreateView, basename='response')

urlpatterns = [
    path('', include(router.urls)),
    path('responses/', response_create, name='response-create'),
    path('user-responses/<int:uid>', ResponseUserList.as_view(), name='response-user-list')
]