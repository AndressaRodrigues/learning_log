from django import forms
from .models import Topic

class TopicForm(forms.ModelsForm):
    class Meta:
        model = Topic
        fiels = ['text']
        labels = {'text': ''}