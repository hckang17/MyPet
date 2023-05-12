from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..form import CommentForm
from ..models import Poster, Comment


@login_required(login_url='common:login')
def comment_create(request, poster_id):
    """
        게시글 답변등록
    """
    poster = get_object_or_404(Poster, pk=poster_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user  # author 속성에 로그인 계정 저장
            comment.create_date = timezone.now()
            comment.poster = poster
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('mypet:detail', poster_id=poster.id), comment.id))
    else:
        form = CommentForm()
    context = {'poster': poster, 'form': form}
    return render(request, 'mypet/post_detail.html', context)



@login_required(login_url='common:login')
def comment_modify(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('mypet:detail', poster_id=comment.poster.id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('mypet:detail', poster_id=comment.poster.id), comment.id))
    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'mypet/comment_form.html', context)


@login_required(login_url='common:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        comment.delete()
    return redirect('mypet:detail', poster_id=comment.poster.id)
