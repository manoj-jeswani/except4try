from django import forms
from .models import Question,Answer

class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'topic',
            "tag_list",
            "detail",
        ]



class AnsForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            
            "detail",
        ]
    