from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import *
from .views import ExchangeTokenView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'api/tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/exchange-token/', ExchangeTokenView.as_view(), name='exchange-token'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)