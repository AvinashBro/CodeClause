from django.db import models

# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=4000) #used to store Character Field
    taskDesc = models.TextField()#Used to store text
    time     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskTitle