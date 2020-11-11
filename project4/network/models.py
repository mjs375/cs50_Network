from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
        # (inherits username, email, password from AbstractUser)
    #--Who is the User following?
    following = models.ManyToManyField("self", symmetrical=False, related_name="user_follower")
        # self-referencing Foreign-key: "self"
        # symmetrical: i.e. user1 follows user2, user2 doesn't follow user1 (default is true)



class Post(models.Model):
    #--What user created the post (ForeignKey => class User)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_user")
    #--The content of the post:
    msg = models.CharField(max_length=160)
    #--Automatically add timestamp as of object creation
    timestamp = models.DateTimeField(auto_now_add=True)
    #--Who liked the post?
    likers = models.ManyToManyField("User", related_name="post_likers")
    #--EMOJI FIELD: every post gets x1 'headliner' emoji
