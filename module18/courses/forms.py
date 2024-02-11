from django import forms
from django.contrib.auth.models import User

from .models import Courses, Comment


class AddCourseForm(forms.ModelForm):
    slug = forms.SlugField(required=True, label='URL', widget=forms.TextInput(attrs={'class': 'form-control'}))
    title = forms.CharField(required=True, label='Title', widget=forms.TextInput(attrs={'class': 'form-control'}))
    desc = forms.CharField(required=True, label='Description', widget=forms.Textarea(attrs={'class': 'form-control'}))
    img = forms.ImageField(required=False, label='Image', widget=forms.FileInput(attrs={'class': 'form-control-file mt-2'}))

    class Meta:
        model = Courses
        fields = ['slug', 'title', 'desc', 'img']


class AddCommentForm(forms.ModelForm):
    text = forms.CharField(required=True, label='Comment', widget=forms.Textarea())
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.HiddenInput()
    )
    course = forms.ModelChoiceField(
        queryset=Courses.objects.all(),
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Comment
        fields = ['text', 'user', 'course']