from django.urls import path, include
from rest_framework.routers import DefaultRouter

from polls import views


router = DefaultRouter()
router.register('paper', views.PaperViewSet)
router.register('comment', views.CommentViewSet)
router.register('login', views.LoginViewSet)

urlpatterns = [
    path('', include(router.urls)),
]