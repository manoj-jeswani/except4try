from django.db import models
from qa.models import Question,Answer
from users.models import Euser

class Comment(models.Model):
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)
    que = models.ForeignKey(Question, null = True, blank = True)
    ans = models.ForeignKey(Answer, null = True, blank = True)
    user = models.ForeignKey(Euser, null = True, blank = True)
    votes=models.IntegerField(default=0)
    upvoters=models.ManyToManyField(Euser, related_name='cmnt_upvoters_list',blank=True)
    downvoters=models.ManyToManyField(Euser, related_name='cmnt_downvoters_list',blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering=['-timestamp']