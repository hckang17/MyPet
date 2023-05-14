from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..form import PosterForm
from ..models import Poster

@login_required(login_url='common:login')
def poster_create(request):
    if request.method == 'POST':
        form = PosterForm(request.POST)
        if form.is_valid():  # 폼이 유효하다면
            poster = form.save(commit=False)  # 임시 저장하여 question 객체를 리턴받는다.
            poster.author = request.user
            poster.create_date = timezone.now()  # 실제 저장을 위해 작성일시를 설정한다.
            poster.save()  # 데이터를 실제로 저장한다.
            return redirect('mypet:index')
        else:   #폼이 잘못되었을 경우
            messages.error(request,'오류가 발생했습니다.')
            form = PosterForm(request.POST)
    else:
        form = PosterForm()
    context = {'form': form}
    return render(request, 'mypet/post_form.html', context)


@login_required(login_url='common:login')
def poster_modify(request, poster_id):
    poster = get_object_or_404(Poster, pk=poster_id)
    if request.user != poster.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('mypet:detail', poster_id=poster.id)
    if request.method == "POST":
        form = PosterForm(request.POST, instance=poster)
        if form.is_valid():
            poster = form.save(commit=False)      # commit = False는 임시저장
            poster.modify_date = timezone.now()  # 수정일시 저장
            poster.save()
            return redirect('mypet:detail', poster_id=poster.id)
    else:
        form = PosterForm(instance=poster)
    context = {'form': form}
    return render(request, 'mypet/post_form.html', context)


@login_required(login_url='common:login')
def poster_delete(request, poster_id):
    poster = get_object_or_404(Poster, pk=poster_id)
    if request.user != poster.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('mypet:detail', poster_id=poster.id)
    poster.delete()
    return redirect('mypet:index')