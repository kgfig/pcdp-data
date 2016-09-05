from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Assessment(models.Model):
    title = models.CharField(max_length=64)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=True, null=True)
    original_id = models.IntegerField()
    type = models.IntegerField()

    def __str__(self):
        return self.title

class Question(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    content = models.TextField()
    original_id = models.IntegerField()
    seq_num = models.IntegerField()
    points = models.IntegerField(default=1)

    def __str__(self):
        return "%d:%s" % (self.original_id, self.content,)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    original_id = models.IntegerField()
    letter = models.CharField(max_length=1)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return "%d:%s" % (self.original_id, self.content,)

class User(models.Model):
    firstname = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    email = models.EmailField()
    original_id = models.IntegerField()
    answers = models.ManyToManyField(Choice)

    def __str__(self):
        return self.username

