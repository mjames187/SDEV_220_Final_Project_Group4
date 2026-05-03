from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Prefetch
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .models import Club
from .models import Post
from .models import reply
from .forms import ClubForm, PostForm, ReplyForm, FilterForm


# Create your views here.
def club_list(request):
    filt_input = request.GET.get('search') if request.GET.get('search') else ''
    if filt_input:
        clubs = Club.objects.filter(Q(title__icontains=filt_input) | Q(description__icontains=filt_input) | Q(sponsor__icontains=filt_input), published_date__lte=timezone.now()).order_by('published_date')
    else:
        clubs = Club.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'clubboard/club_list.html', {'clubs': clubs})

def club_detail(request, pk):
    club = get_object_or_404(Club, pk=pk)
    posts = club.posts.filter(published_date__lte=timezone.now()).order_by('-created_date').prefetch_related('replies')
    user_allowed = True
    if request.method == 'POST' and 'add_interest' in request.POST:
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            for item in club.int_users:
                if item == str(request.user):
                    club.interest -= 1
                    club.int_users.remove(item)
                    club.save()
                    user_allowed = False
            if user_allowed:
                club.interest += 1
                club.int_users.append(str(request.user))
                club.save()
            
    return render(request, 'clubboard/club_detail.html', {'club': club, 'posts': posts})   

def club_new(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = ClubForm(request.POST)
        if form.is_valid():
            club = form.save(commit=False)
            club.authors = request.user
            club.published_date = timezone.now()
            club.interest = 0
            club.int_users = []
            club.save()
            return redirect('club_list')
    else:
        form = ClubForm()
    return render(request, 'clubboard/club_edit.html', {'form': form})

def post_new(request, club_pk):
    if not request.user.is_authenticated:
        return redirect('login')  
    
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

def reply_new(request, post_pk):
    if not request.user.is_authenticated:
        return redirect(f'/accounts/login/?next=/post/{post_pk}/reply/new/')  
    
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply_obj = form.save(commit=False)
            reply_obj.authors = request.user
            reply_obj.post = post
            reply_obj.published_date = timezone.now()
            reply_obj.save()
            return redirect('club_detail', pk=post.club.pk)
    else:
        form = ReplyForm()
    return render(request, 'clubboard/reply_edit.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')
