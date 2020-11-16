
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    #   #   #   #   #   #   #   #   #   #   #   #   #
    # Post a new Squeak:
    path("squeak", views.squeak, name="squeak"),
    # Go to user's profile page:
    path("profile/<str:user>", views.profile, name="profile"),
    # Edit a SQUEAK
    path("edit/<int:post_id>", views.edit, name="edit"),

]


"""
<a href="{% url 'profile' post.user %}">
    - This means, go to [name="profile"],
    - run views.profile,
    -and return the URL path "profile/<str:user>" (whatever you want)

"""
