from django.db import models

# Create your models here.
class TodoList(models.Model):
    td_id=models.AutoField(primary_key=True)
    task_name=models.CharField(max_length=100)
    task_decription=models.TextField()

    def __str__(self) -> str:
        return self.task_name
    