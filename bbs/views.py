from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from bbs import models
from bbs import utils
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
import json
from django.contrib.auth import authenticate, login

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def account_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            user.userprofile.online = True
            user.userprofile.save()
            return HttpResponseRedirect("/")
        else:
            login_err = 'Wrong username or password!'
            return render(request, 'login.html', locals())


def index(request):
    articles = models.Article.objects.all().order_by('-create_on')
    paginator = Paginator(articles, 4)  # Show 4 contacts per page

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    # print(articles)
    return render(request, 'index.html', locals())


def life(request):
    return render(request, 'life.html')


def tech(request):
    return render(request, 'tech.html')


def category1024(request):
    return render(request, '1024.html')


def article(request, article_id):
    error_msg = ''

    try:
        art = models.Article.objects.get(id=article_id)
    except ObjectDoesNotExist as e:
        error_msg = e.args[0]
    else:
        comments = utils.ArticleHandler.build_comments_tree(art)
        # print(locals())
        return render(request, 'article.html', locals())


def edit_article(request):
    if request.method == 'GET':
        return render(request, 'article_edit.html', locals())
    elif request.method == 'POST':
        # print(request.POST)
        art_handler = utils.ArticleHandler(request)
        res = art_handler.create()
        return HttpResponse('hi....')
