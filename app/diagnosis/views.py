from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Diagnosis, Category
from .serializers import DiagnosisSerializer, CategorySerializer
from .permissions import AdminOrReadOnly
from rest_framework.authentication import TokenAuthentication


class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminOrReadOnly]
    

    def _params_to_ints(self, qs):
        """Convert a list of strings to integers."""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Retrieve diagnosis for authenticated user."""
        category = self.request.query_params.get('category')
        queryset = self.queryset
        if category:
            category_ids = self._params_to_ints(category)
            queryset = queryset.filter(category__id__in=category_ids)        

        return queryset


    def perform_create(self, serializer):
        """Create a new diagnosis."""
        Diagnosis_code = self.request.data.get('Diagnosis_code')
        category_data = self.request.data.get('category')
        category_code = [category.get('code') for category in category_data]
        full_code = f"{category_code[0]}{Diagnosis_code}"
        serializer.save(Full_code=full_code)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer