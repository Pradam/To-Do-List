from django.db import models

# Create your models here.

OPTIONAL = {'blank': True, 'null': True}


class ToDoWork(models.Model):
    """Model to store all the to do list data."""

    created_on = models.DateField(auto_now_add=True, **OPTIONAL)
    name = models.CharField(max_length=500, **OPTIONAL)
    created_by = models.ForeignKey('auth.User', **OPTIONAL)
    description = models.TextField(**OPTIONAL)
    list_date = models.DateField(**OPTIONAL)
    completed = models.BooleanField(default=False)

    def __str__(self):
        """Return the Name of the To Do list."""
        return '{}'.format(self.name)
