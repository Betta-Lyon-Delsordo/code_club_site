from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    
class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'body',)
    template_name = 'post_edit.html'
    
class PostDetailView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')