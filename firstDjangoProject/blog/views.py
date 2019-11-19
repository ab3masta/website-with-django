from django.shortcuts import render,get_object_or_404
# from .mocs import Post
from .models import Post
from django.http import Http404

def index(request):
    posts = Post.objects.all()
    return render(request,'blog/index.html', {'posts':posts})
def show(request,id):
    posts = get_object_or_404(Post,pk=id)
    # try:
    #     posts = Post.objects.get(pk=id)
    # except:
    #     raise Http404('Sorry,post #{} not found.'.format(id)) 

    return render(request,'blog/show.html',{'post':posts})
