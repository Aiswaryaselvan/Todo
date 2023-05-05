from django.db import models


# Create your models here.
class Mytask(models.Model):
    taskname = models.CharField(max_length=300)
    priority = models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return self.taskname

