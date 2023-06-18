from django import forms
from .models import Post

from django.core.exceptions import ValidationError

class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            # 'author',
        ]

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            # 'author'
        ]

    # def clean(self):
    #     cleaned_data = super().clean()
    #     text = cleaned_data.get('text')
    #     if text is None:
    #         raise ValidationError({
    #             "text": "Enter text!"
    #         })
    #     return cleaned_data