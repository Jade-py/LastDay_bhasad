from django.shortcuts import render, redirect
from .models import Post
from .forms import PostCreateForm, PostUpdateForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


class PostCreate(CreateView, ListView):
    model = Post
    form_class = PostCreateForm
    template_name = 'home.html'
    success_url = reverse_lazy('home')
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()


class PostUpdate(DetailView, UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'update.html'
    success_url = reverse_lazy('home')


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())

