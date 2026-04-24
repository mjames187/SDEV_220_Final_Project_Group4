from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Club
from .models import Post
from .models import reply
from .forms import PostForm


# Create your views here.
def club_list(request):
    clubs = Club.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'clubboard/club_list.html', {'clubs': clubs})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'clubboard/post_list.html', {'posts': posts})

def club_detail(request, pk):
    club = get_object_or_404(Club, pk=pk)
    posts = club.posts.filter(published_date__lte=timezone.now()).order_by('-created_date')
    if request.method == 'POST' and 'add_interest' in request.POST:
        club.interest += 1
        club.save()
    return render(request, 'clubboard/club_detail.html', {'club': club, 'posts': posts})   

def post_new(request, club_pk):
    club = get_object_or_404(Club, pk=club_pk)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.authors = request.user
            post.club = club
            post.published_date = timezone.now()
            post.save()
            return redirect('club_detail', pk=club.pk)
    else:
        form = PostForm()
    return render(request, 'clubboard/post_edit.html', {'form': form})