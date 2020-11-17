from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import forms
from django.views.decorators.csrf import csrf_exempt # # #
import json
from django.http import JsonResponse

from .models import User, Post, Follow
from .forms import NewPostForm







def index(request):
    form = NewPostForm(initial={'user': request.user}) # create new squeak form instance
    posts = Post.objects.order_by('-timestamp').all() # get ALL posts
        # .reverse() works too
    return render(request, "network/index.html", {
        "form": form,
        "posts": posts, #Post.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")



# NewPostForm is defined in "network/forms.py"
@login_required
def squeak(request):
    if request.method == "GET":
        return render(request, "network/index.html", {
            "form": NewPostForm(initial={'user': request.user}),
        })
    # Compose a new squeak, must be via POST:
    else: # request.method == "POST" (form is submitted)
        form = NewPostForm(request.POST) # create instance of form from POST data
        if form.is_valid(): # validate form
            form.save() # save the new Squeak object
        return index(request)





# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # F E A T U R E # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

@csrf_exempt # @login_required
def edit(request, post_id):
    print("Editing...")
    if request.method == "PUT":
        post = Post.objects.get(user=request.user, pk=post_id)
        content = json.loads(request.body)
        post.message = content["message"]
        post.save()
        return HttpResponse(status=204)




# Load the user's profile page:
# @login_required
def profile(request, user):
    if request.method == "GET":
        print("User:",user)
        username = User.objects.get(username=user) # get User object
        user_posts = Post.objects.filter(user=username.id).order_by('-timestamp') # access posts by Post's
        return render(request, "network/profile.html", {
            # User's own posts:
            "posts": user_posts,
            "username": username,
        })
    else: #
        pass


@login_required
def follow(request, user):
    if request.method == "GET":
        #--Get Username
        username = User.objects.get(username=user) # get User object
        #--Get ALL followed users of User
        followfolks = Follow.objects.filter(follower=user)
        #--Get ALL followed users' posts of User
        followposts = Post.objects.filter(user=followfolks.id)
        return render(request, "network/follow.html", {

        })





# Process each Squeak for #keyword tags
def hashtags():
    pass

# Process each Squeak for @users tags
def usertags():
    pass


#
