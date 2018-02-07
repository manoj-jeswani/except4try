from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Euser(User):

	class Meta:
		verbose_name = 'Euser'

	def __str__(self):
		return self.username

	def get_absolute_url(self):
		return reverse("users:profile",kwargs={"id":self.id})


    # def get_absolute_url(self):
    #     return reverse("person_detail",kwargs={"id":self.bhamashah})
