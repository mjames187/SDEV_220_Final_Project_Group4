from django import forms

from .models import Club, Post, reply

class ClubForm(forms.ModelForm):

    class Meta:
        model = Club
        fields = ('title','location','days','start_time','end_time','sponsor','description',)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('text',)

class ReplyForm(forms.ModelForm):

    class Meta:
        model = reply
        fields = ('text',)

class FilterForm(forms.ModelForm):

    class Meta:
        model = Club
        fields = ('start_time','end_time')
