from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.hashers import make_password

from .models import *
from .forms import *


# Create your views here.
class IndexView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))
        posts = Post.objects.all().order_by("-publish_time")
        post_count = posts.count()
        try:
            page = int(request.GET.get('page', 1))
        except PageNotAnInteger:
            page = 1
        if page < 0:
            page = 1

        p = Paginator(posts, 10, request=request)
        posts = p.page(page).object_list
        page_num = int(post_count / 10)
        if post_count % 10 != 0:
            page_num += 1

        return render(request, 'index.html', {
            "posts": posts,
            "page": page,
            "page_num": page_num,
            "username": request.user.username
        })


class LoginView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, "login.html", {})
        else:
            return render(request, "index", {
                "username": request.user.username
            })

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "login.html")
        else:
            return render(request, "login.html")


class LogoutView(View):
    """
    用户登出
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("login"))


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            password1 = request.POST.get("password1", "")
            password2 = request.POST.get("password2", "")
            username = request.POST.get("username", "")
            if password1 != password2:
                return render(request, "register.html", {"register_form": register_form, "msg": "两次输入密码不匹配"})
            if User.objects.filter(username=username):
                return render(request, "register.html", {"register_form": register_form, "msg": "用户已经存在"})
            user = User()
            user.username = username
            user.password = make_password(password1)
            user.save()
            return render(request, "login.html")
        else:
            return render(request, "register.html", {"register_form": register_form})


class PublishView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))
        return render(request, "publish_post.html", {
            "username": request.user.username
        })

    def post(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))
        title = request.POST.get("title", "")
        if title == "":
            title = "我发布了一条任务~"
        content = request.POST.get("content", "")
        post_info = Post()
        post_info.title = title
        post_info.author = request.user
        post_info.content = content
        post_info.save()
        return HttpResponseRedirect(reverse("index"))


class PostView(View):
    def get(self, request, id):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))
        try:
            post_info = Post.objects.get(id=id)
        except Exception:
            return render(request, "404.html")

        return render(request, "todo.html", {
            "post_info": post_info,
            "username": request.user.username
        })

    def post(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))


class DeleteView(View):
    def get(self, request, id):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))
        try:
            post_info = Post.objects.get(id=id)
        except Exception:
            return
        if post_info.author.username != request.user.username:
            return
        post_info.delete()
        return HttpResponseRedirect(reverse("index"))


class SettingView(View):
    def get(self, request, id):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))
        try:
            post_info = Post.objects.get(id=id)
        except Exception:
            return
        if post_info.author.username != request.user.username:
            return
        return render(request, "setting_post.html", {
            "username": request.user.username,
            "title": post_info.title,
            "content": post_info.content,
            "id": id,
        })

    def post(self, request, id):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))
        try:
            post_info = Post.objects.get(id=id)
        except Exception:
            return
        if post_info.author.username != request.user.username:
            return
        title = request.POST.get("title", "")
        if title == "":
            title = "我发布了一条任务~"
        content = request.POST.get("content", "")
        post_info.title = title
        post_info.content = content
        post_info.save()
        return HttpResponseRedirect(reverse("index"))