from django.contrib.auth.models import AbstractUser
from django.db import models

"""
$ python3 manage.py makemigrations
    ( $ python3 manage.py makemigrations [app name] )
        - first migrations^^
$ python3 manage.py migrate
$ python3 manage.py runserver
    -Run the app
"""

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
    message = models.CharField(max_length=160)
    #--Automatically add timestamp as of object creation
    timestamp = models.DateTimeField(auto_now_add=True)
    #--Who liked the post?
    # likers = models.ManyToManyField("User", related_name="post_likers", blank=True)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

"""
class Hashtag(models.Model):
    #--Which user used the hashtag:
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hashtag_user")
    #--Which post contains the hashtag:
    hashpost = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="hashtag_post")
    #--The hashtag itself (...)
    hashtag = models.CharField(max_length=160)


class Usertag(models.Model):
    #--Which user made the @user tag:
    tagger = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usertag_tagger")
    #--Which user was tagged by @user:
    tagged = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usertag_tagged")
    #--Which post contains the @user tag:
    usertagpost = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="usertag_post")

class Profile(models.Model):
    profileUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile_user")
"""

#
