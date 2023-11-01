from django import forms
from django.forms import CheckboxSelectMultiple
from.models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'