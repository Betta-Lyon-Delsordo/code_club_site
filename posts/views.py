from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
def redirect_view(request):
    response = redirect('users/login/')
    return response

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
 
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ('title', 'body', 'cover',)
    template_name = 'post_edit.html'
    login_url = 'login'
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
    login_url = 'login'
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ('title', 'body', 'author', 'cover',)
    login_url = 'login' 
    
   