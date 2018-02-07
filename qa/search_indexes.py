from haystack import indexes
 
from .models import Question
 
 
class QuestionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    topic =indexes.CharField(model_attr='topic')
    detail= indexes.CharField(model_attr='detail')
 
    def get_model(self):
        return Question
 
    def index_queryset(self, using=None):
        return self.get_model().objects.all()


       