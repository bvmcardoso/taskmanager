from rest_framework import generics, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import TaskList, Task, Tag
from .serializers import TaskListSerializer, TaskSerializer, TagSerializer
from django.db import IntegrityError
import logging 

logger = logging.getLogger('task_api')

class TaskListReadCreate(generics.ListCreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

class TaskListReadUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskListSerializer

    def get_queryset(self):
        task_list = TaskList.objects.filter(pk=self.kwargs['pk'])
        if task_list.exists():
            logger.info('Info') # Esse nível de criticidade não será pego, apenas CRITICAL ou ERROR, por isso não usei os demais! De qualquer forma devolver os http status para o usuário acredito que possa ser considerado como uma forma log.
            logger.critical('Specific Task List read from the database!')     
            return task_list
            
        else:
            raise ValidationError('Error: The tasklist you are looking for does not exist!')
    
    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            logger.critical('Specific Task List removed from the database!')     
            return Response("Tasklist has been deleted successfully!", status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        kwargs['pk'] = True
        self.update(request, *args,**kwargs)
        logger.critical('Specific Task List updated in the database!')     
        return Response("Tasklist has been updated successfully!", status=status.HTTP_204_NO_CONTENT)

class TaskReadCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer    

class TaskReadUpdateDelete(generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = TaskSerializer 

    def get_queryset(self):
        task = Task.objects.filter(pk=self.kwargs['pk'])
        if task.exists():
            logger.critical('Specific task returned from the database!')     
            return task
        else:
            return ValidationError('Error: The task you are looking for does not exist.')

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            logger.critical('Specific task removed from the database!')     
            return Response("Task has been deleted successfully!", status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        kwargs['pk'] = True
        self.update(request, *args, **kwargs)
        logger.critical('Specific task updated in the database!')     
        return Response("Task has been updated successfully", status=status.HTTP_204_NO_CONTENT)
    

class TagReadCreate(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
 


class TagReadUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer

    def get_queryset(self):
        tag = Tag.objects.filter(pk=self.kwargs['pk'])
        if tag.exists():
            logger.critical('Querying specific tag')     
            return tag
    
    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            logger.critical('Tag deletion!')     
            return Response("Tag has been deleted successfully!", status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        kwargs['pk'] = True
        self.update(request, *args,**kwargs)
        logger.critical('Tag update!')     
        return Response("Tasklist has been updated successfully!", status=status.HTTP_204_NO_CONTENT)