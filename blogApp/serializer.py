from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog

        fields = ["id", "title", "content", "status", "user_id", "created_at", "update_at"]

        def create(self, validated_data):
            blog = Blog.objects.create_user(
                id=validated_data.pop('id'),
                title=validated_data.pop('title'),
                content=validated_data.pop('title'),
                status=validated_data.pop('status'),
                user_id=validated_data.pop('user_id'),
                created_at=validated_data.pop('created_at'),
                update_at=validated_data.pop('updated_at'),
            )
            return blog
