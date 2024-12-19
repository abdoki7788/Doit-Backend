from rest_framework import serializers
from .models import List, Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "name", "added_at", "is_done", "in_list", "is_important"]
        read_only_fields = ["id", "added_at", "is_done", "in_list", "is_important"]

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


class ListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = List
        fields = ["id", "name", "tasks"]
        read_only_fields = ["id", "tasks"]
