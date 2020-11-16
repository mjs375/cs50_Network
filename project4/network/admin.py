from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Post #class, class

"""
$ python3 manage.py createsuperuser
  - Enter username, email, password.
$ python3 manage.py runserver
  - Navigate to http://127.0.0.1:8000/admin to go to the native Django administrative page. Easily create, edit, and delete objects stored in the DB.
"""




# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("user", "message", "timestamp")



# register your models here to manipulate in the Admin interface:
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
