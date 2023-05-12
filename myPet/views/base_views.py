from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Poster

def index(request):
    page = request.GET.get('page', '1')  # page
    KeyWord = request.GET.get('kw', '')
    poster_lists = Poster.objects.order_by('create_date')
    if (KeyWord):
        poster_lists=poster_lists.filter(
            Q(subject__icontains=KeyWord)|
            Q(content__icontains=KeyWord)|
            Q(comment__content__icontains=KeyWord)|
            Q(author__username__icontains=KeyWord)|
            Q(comment__author__username__icontains=KeyWord)
        ).distinct()
    paginator = Paginator(poster_lists, 10)
    page_obj = paginator.get_page(page)
    context = {'post_list': page_obj, 'page_obj': page, 'kw': KeyWord }
    return render(request, 'mypet/post_list.html', context)


def detail(request, poster_id):
    poster = get_object_or_404(Poster, pk=poster_id)
    context = {'poster': poster}
    return render(request, 'mypet/post_detail.html', context)