from django.contrib import admin
from django.urls import path
from tasks import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    # TaskLists
    path('taskList', views.TaskListReadCreate.as_view()),
    path('taskList/<uuid:pk>', views.TaskListReadUpdateDelete.as_view()),
    # Tasks:
    path('tasks', views.TaskReadCreate.as_view()),
    path('tasks/<uuid:pk>', views.TaskReadUpdateDelete.as_view()),
    # Tags:
    path('tags', views.TagReadCreate.as_view()),
    path('tags/<uuid:pk>', views.TagReadUpdateDelete.as_view()),
]
