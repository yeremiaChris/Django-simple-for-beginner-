from django.shortcuts import render,redirect
from .models import Comment
from .forms import CommentForm
# Create your views here.
def index(request):
    comment = Comment.objects.order_by('-date_added')
    context = {
        'comment': comment
    }
    return render(request,'guessbook/index.html',context)

def sign(request):

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = Comment(name=request.POST['name'],comment=request.POST['comment'])
            new_comment.save()
            return redirect('index')

    else:
        form = CommentForm()


    form = CommentForm()
    context = {
        'forms': form
    }
    return render(request,'guessbook/sign.html',context)