from rest_framework import serializers
from .models import Diagnosis, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'code']

class DiagnosisSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Diagnosis
        fields = ['id', 'category', 'Diagnosis_code', 'Full_code', 'Abbreviated_description', 'Full_description', 'created_at', 'updated_at']
    def _get_or_create_category(self, category_data, diagnosis):
        """Handle getting or creating category as needed."""
        auth_user = self.context['request'].user
        for category in category_data:
            category_obj, _= Category.objects.get_or_create(
                user=auth_user,
                **category,
            )
            diagnosis.category.add(category_obj)


    def create(self, validated_data):
        """Create a diagnosis."""
        category = validated_data.pop('category', [])
        diagnosis = Diagnosis.objects.create(**validated_data)
        self._get_or_create_category(category, diagnosis)

        return diagnosis

    def update(self, instance, validated_data):
        # """Update diagnosis."""
        category = validated_data.pop('category', None)
        if category is not None:
            instance.category.clear()
            self._get_or_create_category(category, instance)       

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
    