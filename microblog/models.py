from django.db import models

class UserManager(models.Manager):
    def get_query_user(self, name):
        return super(UserManager, self).get_queryset().filter(name__contains=name)


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=True)
    email = models.EmailField(max_length=64)
    blogs = models.ManyToManyField('Blog')
    manager = UserManager()
    objects = models.Manager()

    def __unicode__(self):
        return self.name

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    content = models.TextField()
    def __unicode__(self):
        return self.title

