from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Assessment(models.Model):
    title = models.CharField(max_length=128)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=True, null=True)
    original_id = models.IntegerField()
    type = models.IntegerField()

    def __str__(self):
        return self.title
