from django import forms
from myPet.models import *

class PosterForm(forms.ModelForm):
    class Meta:
        model = Poster    #사용할 모델
        fields = ['subject', 'content'] #QuestionForm에서 사용할 Model속성
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }

