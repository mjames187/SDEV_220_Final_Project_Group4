from django import forms

from .models import Post, reply

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('text',)

class ReplyForm(forms.ModelForm):

    class Meta:
        model = reply
        fields = ('text',)
