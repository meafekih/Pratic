
from django.urls import path, include
from .views import home, BlogViewSet, CategorieViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('blogs', BlogViewSet)
router.register('categories', CategorieViewSet)

urlpatterns=[
    path('', home, name='home'),
    path('', include(router.urls)),
]