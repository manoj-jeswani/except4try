from django.db import models
from users.models import Euser


class Category(models.Model):
	tag= models.CharField(max_length=50)

	class Meta:
		verbose_name = 'Category'

	def __str__(self):
		return self.tag




class Qabase(models.Model):
	detail=models.TextField(max_length=2000)
	votes = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	user=models.ForeignKey(Euser,on_delete=models.CASCADE)


class Answer(Qabase):

	class Meta:
		verbose_name = 'Answer'

	def __str__(self):
		return self.user.username + " : " + self.detail



class Question(Qabase):
	topic=models.CharField(max_length=100)
	tag_list=models.ManyToManyField(Category)
	ans_list=models.ManyToManyField(Answer,blank=True)
	


	class Meta:
		verbose_name = 'Question'

	def __str__(self):
		return self.topic

