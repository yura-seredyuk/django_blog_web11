from django import forms
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from blog.models import Post

from .forms import PostForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout


def home(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/pages/index.html', {'posts':posts})

def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/pages/post_details.html', {'post':post})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post:
        post.delete()
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'blog/pages/index.html', {'posts':posts})

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm()
    return render(request,'blog/pages/post_edit.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request,'blog/pages/post_edit.html', 
                            {'form':form,
                            'pk': pk})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            client_data = form.cleaned_data
            user = authenticate(username = client_data['username'],
                                password = client_data['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    # return HttpResponse('Authenticated successful!')
                    return redirect('home')
                else:
                    return HttpResponse('User is blocked!')
            else:
                return HttpResponse('User not found!')
    else:
        form = LoginForm()
    return render(request, 'blog/pages/login.html', {'form':form})


def user_logout():
    pass