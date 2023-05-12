from django.urls import path
from .views import base_views, poster_views, comment_views


app_name = 'mypet'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:poster_id>/',
         base_views.detail, name='detail'),

    # poster_views.py
    path('poster/create/',
         poster_views.poster_create, name='poster_create'),
    path('poster/modify/<int:poster_id>/',
         poster_views.poster_modify, name='poster_modify'),
    path('poster/delete/<int:poster_id>/',
         poster_views.poster_delete, name='poster_delete'),

    # comment_views.py
    path('answer/create/<int:poster_id>/',
         comment_views.comment_create, name='comment_create'),
    path('answer/modify/<int:comment_id>/',
         comment_views.comment_modify, name='comment_modify'),
    path('answer/delete/<int:comment_id>/',
         comment_views.comment_delete, name='comment_delete'),
]