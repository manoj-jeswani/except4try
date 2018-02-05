from django import forms
from .models import Question

class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'topic',
            "tag_list",
            "detail",
        ]
    