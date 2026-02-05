from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    STATUS_CHOICES = [
        ('Planned', 'Planned'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Planned')
    technology = models.ManyToManyField(Technology, blank=True)  # <-- change here
    what_i_learned = models.TextField()

    def __str__(self):
        return self.name