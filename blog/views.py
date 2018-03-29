from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    all_posts = Post.objects.all()
    return render(request ,'blog/index.html',{'posts':all_posts})