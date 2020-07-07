from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Comment
from django.utils import timezone
from .form import BlogForm

# Create your views here.
def list(request):
    blogs = Blog.objects.all() 
    return render(request, 'list.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    comments = Comment.objects.filter(blog=blog)
    like_num = len(blog.like.all())
    liker = (blog.like.all()[0] if like_num>0 else '')
    islike = (True if request.user in blog.like.all() else False)
    return render(request, 'detail.html', {
        'blog':blog, 
        'comments':comments,
        'liker':liker, 
        'likes':like_num,
        'islike': islike})

def commenting(request, blog_id):
    new_comment = Comment()
    new_comment.blog = get_object_or_404(Blog, pk=blog_id)
    new_comment.author = request.user
    new_comment.body = request.POST.get('body')
    new_comment.save()
    return redirect('/blog/'+str(blog_id))

  
def comment_delete(request, blog_id, comment_id):
    delete_comment = get_object_or_404(Comment, pk=comment_id)
    delete_comment.delete()
    return redirect('/blog/'+str(blog_id))

def like(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.user in blog.like.all():
        blog.like.set(blog.like.exclude(username=request.user))
    else : 
        blog.like.add(request.user)
    blog.save()
    return redirect('/blog/'+str(blog_id))

def new(request):
    if request.method =='POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.pub_date = timezone.now()
            content.save()
            return redirect('list')
    else:
        form = BlogForm()
        return render(request, 'new.html', {'form':form})

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.pub_date = timezone.datetime.now()
    new_blog.body = request.POST['body']
    new_blog.save()
    return redirect('/blog/'+str(new_blog.id))

def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'blog':edit_blog})

def update(request, blog_id):
    update_blog = get_object_or_404(Blog, pk=blog_id)
    update_blog.title = request.POST['title']
    update_blog.pub_date = timezone.datetime.now()
    update_blog.body = request.POST['body']
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request, blog_id):
    delete_blog = get_object_or_404(Blog, pk=blog_id)
    delete_blog.delete()
    return redirect('list')