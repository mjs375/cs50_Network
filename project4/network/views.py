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
from django.core.paginator import Paginator

from .models import User, Post, Follow
from .forms import NewPostForm







def index(request):
    form = NewPostForm(initial={'postuser': request.user}) # create new squeak form instance
    posts = Post.objects.order_by('-timestamp').all() # get ALL posts / .reverse() works too
    #--PAGINATION (show 10 posts per page)
    page_obj = paginate(request, posts)
    return render(request, "network/index.html", {
        "form": form,
        #"posts": posts, #Post.objects.all()
        "page_obj": page_obj,
    })


def paginate(request, posts):
    paginator =  Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


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
        post = Post.objects.get(postuser=request.user, pk=post_id)
        content = json.loads(request.body)
        post.message = content["message"]
        post.save()
        return HttpResponse(status=204)




#--Load the user's profile page:
# @login_required
def profile(request, username):
    if request.method == "GET":
        uprofile = User.objects.get(username=username) # get profileuser object
        getfollowers = Follow.objects.filter(followed=uprofile.id) #.count()
        checkfollow = [User.objects.get(pk=f.follower.id) for f in getfollowers]
        iamfollowing = Follow.objects.filter(follower=uprofile.id)#.count()
        user_posts = Post.objects.filter(postuser=uprofile.id).order_by('-timestamp') # access posts by Post's
        #--Paginate the posts:
        page_obj = paginate(request, user_posts)
        return render(request, "network/profile.html", {
            # User's own posts:
            "page_obj": page_obj, # user_posts,
            "username": uprofile,
            "followers": getfollowers,
            "checkfollow": checkfollow,
            "following": iamfollowing,
        })
    else: #
        pass


@login_required
def follow(request):
    #--Get all [follows] YOU are [in/]following:
    fs = Follow.objects.filter(follower=request.user)
    # Get all user.ids of those Follow objects:
    fusers = [f.followed for f in fs]
    #--Get all posts from list of followed-users.id:
    posts = Post.objects.filter(postuser__in=fusers).order_by('timestamp').reverse()
    page_obj = paginate(request, posts)
    return render(request, "network/follow.html", {
        "page_obj": page_obj,
    })


@login_required
@csrf_exempt
def like(request, id):
    post = Post.objects.get(pk=id)
    if request.method == "PUT":
        print("LIKING...")
        if request.user in post.likedby.all(): #UNLIKE
            #UNlike
            post.likedby.remove(request.user) #add/remove b/c a SET!
            post.save()
            print("Changed to unlike")
            return HttpResponse(status=204)
        else: # LIKE
            post.likedby.add(request.user)
            post.save()
            print("Like added.")
            return HttpResponse(status=204)
        #-> Not returning a render template b/c we do NOT want to reload the page after each like/unlike

@login_required
@csrf_exempt
def addfollow(request, username):
    #--Get actual User object from str Username
    tofollow = User.objects.get(username=username)
    #--Is the {request.user} already following {username}?
    follows = Follow.objects.filter(follower=request.user, followed=tofollow)
    if request.method == "PUT":
        if not follows:
            #--Create a model object ( .create() also .save()s. )
            print("Creating following")
            Follow.objects.create(follower=request.user, followed=tofollow)
        else:
            #--Unfollow (delete the model instance)
            print("Deleting following")
            follows.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse() # TODO





#
