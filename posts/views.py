from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post_list.html'
    
    
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ('title', 'body',)
    template_name = 'post_edit.html'
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ('title', 'body',)
    login_url = 'login' 
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_vailid(form)