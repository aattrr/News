from django import forms
from app_users.models import News, Comment, Metatag
# from django.forms import TextInput, Textarea
from django.forms import ModelMultipleChoiceField, Textarea


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'description', 'status', 'metatag']

    metatag = forms.ModelMultipleChoiceField(queryset=Metatag.objects.all(), required=False)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """Установка необязательности - поля USER"""
        super(CommentForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields['user'].required = False
