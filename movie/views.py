from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.core.paginator import Paginator
from django.db.models import Q

import operator

from .models import *


def index(request):
    begin = datetime.now()
    data = Movie.objects.filter().values()
    paginator = Paginator(data, 50)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    end = datetime.now()
    cost = (end - begin).total_seconds()
    page_range = range(max(1, page_number - 2), min(paginator.num_pages, page_number + 5) + 1)
    return render(request, 'movie/index.html', {'posts': page, 'cost': cost, 'page_range': page_range})


def actor_index(request):
    begin = datetime.now()
    data = Actor.objects.filter().values()
    paginator = Paginator(data, 50)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    end = datetime.now()
    cost = (end - begin).total_seconds()
    page_range = range(max(1, page_number - 2), min(paginator.num_pages, page_number + 5) + 1)
    return render(request, 'movie/actorIndex.html', {'posts': page, 'cost': cost, 'page_range': page_range})


def search_place(request):
    return render(request, 'movie/search.html')


def search(request):
    test = request.GET.get('search_class')
    key = request.GET.get('keyword')
    begin = datetime.now()
    if test == "Comment":
        comment_list = Comment.objects.filter(Q(comment__icontains=key))
        paginator = Paginator(comment_list, 25)
        page_number = int(request.GET.get('page', 1))
        page = paginator.get_page(page_number)
        end = datetime.now()
        cost = (end - begin).total_seconds()
        page_range = range(max(1, page_number - 2), min(paginator.num_pages, page_number + 5) + 1)
        return render(request, 'movie/commentIndex.html',
                      {'posts': page, 'cost': cost, 'keyword': key, 'page_range': page_range, 'type': test})

    elif test == "Movie":
        list0 = Movie.objects.filter(Q(film_name__icontains=key) | Q(actor__actor_name__icontains=key))
        film_list = list(set(list0))
        paginator = Paginator(film_list, 25)
        page_number = int(request.GET.get('page', 1))
        page = paginator.get_page(page_number)
        end = datetime.now()
        cost = (end - begin).total_seconds()
        page_range = range(max(1, page_number - 2), min(paginator.num_pages, page_number + 5) + 1)
        return render(request, 'movie/filmSearch.html',
                      {'posts': page, 'cost': cost, 'keyword': key, 'page_range': page_range, 'type': test})
    elif test == "Actor":
        list0 = Actor.objects.filter(Q(actor_name__icontains=key) | Q(movie__film_name__icontains=key))
        actor_list = list(set(list0))
        paginator = Paginator(actor_list, 25)
        page_number = int(request.GET.get('page', 1))
        page = paginator.get_page(page_number)
        end = datetime.now()
        cost = (end - begin).total_seconds()
        page_range = range(max(1, page_number - 2), min(paginator.num_pages, page_number + 5) + 1)
        return render(request, 'movie/actorSearch.html',
                      {'posts': page, 'cost': cost, 'keyword': key, 'page_range': page_range, 'type': test})



def film(request, film_num):
    return render(request, 'movie/filmdetail.html', {'post': get_object_or_404(Movie, film_number=film_num)})


def actor(request, actor_num):
    act = Actor.objects.get(actor_number=actor_num)
    ls = act.movie_set.filter()
    related_actor = []
    for a in ls:
        related_actor += a.actor.filter(~Q(actor_number=act.actor_number))
    set_a = list(set(related_actor))
    count_set_a = {}
    for item in set_a:
        count_set_a[item] = related_actor.count(item)
    sorted_list_a = sorted(count_set_a.items(), key=operator.itemgetter(1))

    result_a = []  # 存放最后的结果
    i = 0
    for item in sorted_list_a[::-1]:  # 按value值从大到小排序
        if i < 10:
            result_a.append(item)
            i += 1
    return render(request, 'movie/actordetail.html', {'post': get_object_or_404(Actor, actor_number=actor_num),
                                                      'related': result_a})
