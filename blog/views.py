from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
#in a view we choose what model to display in the template
#to take actual object from the model we need QuerySet
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
