# blog/views.py

from django.shortcuts import render
from .forms import PostForm

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            pass
    else:
        form = PostForm()
    
    return render(request, 'blog/post_form.html', {
        'form': form,
    })
