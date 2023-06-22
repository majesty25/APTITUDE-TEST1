"""
URL mappings for the recipe app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from .views import DiagnosisViewSet


router = DefaultRouter()
router.register('diagnosis', DiagnosisViewSet)
# router.register('tags', views.TagViewSet)
# router.register('ingredients', views.IngredientViewSet)

app_name = 'diagnosis'

urlpatterns = [
    path('', include(router.urls)),
]