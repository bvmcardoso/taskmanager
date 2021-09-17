from django.test import TestCase
from .models import Tag, TaskList, Task

class TestTag(TestCase):

    def test_tag_creation(self):
        tag = Tag.objects.create(name="Tag 4")
        last_tag = Tag.objects.last()
        self.assertEqual(last_tag.name, "Tag 4")

    def test_task_list_creation(self):
        task_list = TaskList.objects.create(name="Walk the dog")
        last_task_list = TaskList.objects.last()
        self.assertEqual(last_task_list.name, "Walk the dog")
    
  
