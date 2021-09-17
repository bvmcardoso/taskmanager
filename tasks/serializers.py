from rest_framework import serializers 
from .models import TaskList,Task,Tag

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = ['id','name']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields = [ 'id', 'title', 'notes', 'priority', 'remind_me_on', 'activity_type', 'status', 'tasklist', 'tags']

class TagSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(source='tagged.count', read_only=True)

    class Meta:
        model = Tag
        fields = ['id', 'name', 'count']
        read_only_fields = ['count']
        