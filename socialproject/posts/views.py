import json
from django.shortcuts import render, redirect
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Post, Comment

# Create your views here.

@login_required
def create_post(request):
  if request.method == "POST":
    form = PostCreateForm(data=request.POST, files=request.FILES)
    if form.is_valid():
      new_post = form.save(commit=False)
      new_post.user = request.user
      new_post.save()
  else:
    form = PostCreateForm()
  return render(request, "posts/create.html", {"form": form})

@login_required
def index(request):
  posts = Post.objects.all()#filter(user=request.user)
  logged_user = request.user
  return render(request, "posts/index.html", {"posts":posts, "logged_user": logged_user})

def feed(request):
  posts = Post.objects.all()
  return render(request, "posts/feed.html",{"posts":posts})

def like_post(request):
      jsonData = json.loads(request.body)
      postid = jsonData.get("post_id")
      post = Post.objects.get(id = postid)
      if post.liked_by.filter(id=request.user.id).exists():
        post.liked_by.remove(request.user)
      else:
        post.liked_by.add(request.user)
      return redirect("/posts")
    
def comment_post(request):
      jsonData = json.loads(request.body)
      postid = jsonData.get("post_id")
      post = Post.objects.get(id = postid)
      commentbody = jsonData.get("comment_body")
      comment = Comment.objects.create(body=commentbody, user = request.user)
      comment.post = post
      comment.save()
      
def like_post(request):
      jsonData = json.loads(request.body)
      comment_id = jsonData.get("comment_id")
      comment = Comment.objects.get(id = comment_id)
      if comment.liked_by.filter(id=request.user.id).exists():
        comment.liked_by.remove(request.user)
      else:
        comment.liked_by.add(request.user)
      return redirect("/posts")