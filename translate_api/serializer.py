from .models import ParentCategory
from rest_framework import serializers

class GetParentCategorySerializer(serializers.ModelSerializer):
    """
    serializer for parent category 
    """

    class Meta:
        model = ParentCategory
        fields = ["id", "title", "thumbnail_img"]