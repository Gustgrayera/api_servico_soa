from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    adress = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    website = models.CharField(max_length=100)

def __str__(self):
    return self.name

class Todos(models.Model):
    userid = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(False)

class Post(models.Model):
    userid = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=300)

class Comment(models.Model):
    postid = models.ForeignKey(Post, on_delete = models.CASCADE)
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    body = models.CharField(max_length=300)