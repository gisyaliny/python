from django.forms import BaseModelForm
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import CreateView,DeleteView,DetailView,UpdateView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all().order_by('-date_posted')
    }
    return render(request, 'blog/home.html', context)

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False
    
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog-home')
    
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False

def about(request):
    return render(request,"blog/about.html")




