# Generated by Django 3.0.6 on 2021-09-15 21:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('notes', models.CharField(max_length=255)),
                ('priority', models.IntegerField()),
                ('remind_me_on', models.DateField()),
                ('activity_type', models.CharField(choices=[('1', 'indoors'), ('2', 'outdoors')], default='1', max_length=2)),
                ('status', models.CharField(choices=[('1', 'open'), ('2', 'done')], default='1', max_length=2)),
                ('tags', models.ManyToManyField(to='tasks.Tag')),
                ('tasklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.TaskList')),
            ],
        ),
    ]
