from django.shortcuts import render
from .models import post

# Create your views here.
def post_list(request):
    posts = post.objects.all().order_by('-date')
    return render(request, 'post/post_list.html', {'posts': posts})