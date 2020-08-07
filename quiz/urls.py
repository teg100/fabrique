from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'quizes', QuizViewSet, basename='quiz')
router.register('questions', QuestionViewSet)
response_create = ResponseCreateView.as_view({'post': 'create'})

schema_view = get_schema_view(
   openapi.Info(
      title="Quiz API",
      default_version='v1',
      description="API documentation",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)
# router.register('responses', ResponseCreateView, basename='response')

urlpatterns = [
    path('responses/', response_create, name='response-create'),
    path('user-responses/<int:uid>', ResponseUserList.as_view(), name='response-user-list'),
    path(r'docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(router.urls)),
]