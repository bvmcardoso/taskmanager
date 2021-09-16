from django.db import models
import uuid

class TaskList(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)    


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    count = models.IntegerField()


class Task(models.Model):
    class Activity(models.TextChoices):
        indoors = '1', "indoors"
        outdoors = '2', "outdoors"

    class Status(models.TextChoices):
        open = '1',"open"
        done = '2',"done"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    priority = models.IntegerField()
    remind_me_on = models.DateField()
    activity_type = models.CharField(max_length=2, choices=Activity.choices, default=Activity.indoors)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.open)
    tasklist = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)


