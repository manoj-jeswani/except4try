from django.db import models
from users.models import Euser
from django.urls import reverse


class Category(models.Model):
	tag= models.CharField(max_length=50)

	class Meta:
		verbose_name = 'Category'

	def __str__(self):
		return self.tag

	def get_absolute_url(self):
		return reverse("home:tag_detail",kwargs={"id":self.id})



class Qabase(models.Model):
	detail=models.TextField(max_length=2000)
	votes = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	user=models.ForeignKey(Euser,on_delete=models.CASCADE)
	upvoters=models.ManyToManyField(Euser, related_name='upvoters_list',blank=True)
	downvoters=models.ManyToManyField(Euser, related_name='downvoters_list',blank=True)
	

class Answer(Qabase):

	class Meta:
		verbose_name = 'Answer'
		ordering=['-timestamp']


	def __str__(self):
		return self.user.username + " : " + self.detail

	def get_uname(self):
		return self.user.username

	def get_upvoters(self):
		qset=self.upvoters.all()
		res=[]
		for uobj in qset:
			res.append(uobj.username)

		return res		

	def get_downvoters(self):
		qset=self.downvoters.all()
		res=[]
		for uobj in qset:
			res.append(uobj.username)

		return res		


class Question(Qabase):
	topic=models.CharField(max_length=100)
	tag_list=models.ManyToManyField(Category)
	ans_list=models.ManyToManyField(Answer,blank=True)
	


	class Meta:
		verbose_name = 'Question'
		ordering=['-timestamp']

	def __str__(self):
		return self.topic

	def get_absolute_url(self):
		return reverse("qa:qdetail",kwargs={"id":self.id})
	
	def get_uname(self):
		return self.user.username


	def get_upvoters(self):
		qset=self.upvoters.all()
		res=[]
		for uobj in qset:
			res.append(uobj.username)

		return res		

	def get_downvoters(self):
		qset=self.downvoters.all()
		res=[]
		for uobj in qset:
			res.append(uobj.username)

		return res		

	def get_ans_count(self):
		return self.ans_list.count()
	
	def get_tag_list(self):
		qset=self.tag_list.all()
		res=[]
		for cobj in qset:
			res.append(cobj.tag)
		return res
	