# blog/views.py

from django.shortcuts import redirect, render
from .forms import PostForm
from .models import Post

def post_new(request):
    form_cls = PostForm
    template_name = 'myapp/post_form.html'
    success_url = '/blog/'

    if request.method == 'POST':
        form = form_cls(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(success_url)
    else:
        form = form_cls()
    
    return render(request, template_name, {
        'form': form,
    })
