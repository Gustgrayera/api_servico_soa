from django.contrib import admin

from .models import User, Todos, Post, Comment

admin.site.register(User)
admin.site.register(Todos)
admin.site.register(Post)
admin.site.register(Comment)