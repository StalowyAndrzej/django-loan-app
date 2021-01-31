from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('apps', views.ApprovalsView)
urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.confirm_status_application, name='form'),
] 