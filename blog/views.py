from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

class PostsListView(ListView):
    model = Post

    def get_queryset(self):
        return super(PostsListView, self).get_queryset().filter(published=True)
