from django.db import models
import django.contrib.auth.models
import datetime

class Category(models.Model):
    category = models.CharField(max_length=50)
    ownedBy = models.ForeignKey(django.contrib.auth.models.User)
    def __str__(self):
        return self.category
    class Meta:
        ordering = ['category']

class ToDoItem(models.Model):


    def addWeek(self):
        return datetime.datetime.now() + datetime.timedelta(days=7)

    owner = models.ForeignKey(django.contrib.auth.models.User)
    category = models.ForeignKey(Category, blank=True,  null=True)
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=200, blank=True)
    createdDate = models.DateField(auto_now_add=True)
    lastUpdatedDate = models.DateField(auto_now_add=True)
    nextUpdateDate = models.DateField()
    dropDeadDate = models.DateField( verbose_name="Due Date")
    priority = models.IntegerField()
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['priority']


