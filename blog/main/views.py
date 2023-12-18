from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Profile, Post, Comment
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView




class BBLogoutView(LoginRequiredMixin, LogoutView):
   template_name = 'main/logout.html'

class BBLoginView(LoginView):
   template_name = 'main/login.html'

def home(request):
    posts_list = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts_list, 50)  # Показывать 50 постов на странице

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'main/home.html', {'posts': posts})

def profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    return render(request, 'main/profile.html', {'profile': profile})

def edit_profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    if request.method == 'POST':
        # Обновите профиль здесь
        pass
    return render(request, 'main/edit_profile.html', {'profile': profile})

def delete_profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    if request.method == 'POST':
        profile.delete()
        return redirect('home')
    return render(request, 'main/confirm_delete.html', {'profile': profile})

def edit_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.method == 'POST':
        # Обновите комментарий здесь
        pass
    return render(request, 'main/edit_comment.html', {'comment': comment})

def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('home')
    return render(request, 'main/confirm_delete.html', {'comment': comment})