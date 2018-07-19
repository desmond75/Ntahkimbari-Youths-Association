from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import datetime

class Member(AbstractUser):	
	username = models.PositiveIntegerField(unique=True)
	age = models.DateField(db_index=True, blank=True, null=True)
	photo = models.ImageField(upload_to='photos', blank=True)
	date_joined = models.DateTimeField(default=timezone.now)
	total_household = models.PositiveIntegerField(db_index=True, default=0, db_column='Total Person in your house')
	sex = models.CharField(max_length=9, blank=False, default=None, db_index=True, null=True)

	def __str__(self):
		return str(self.username)

class Community_work(models.Model):
	where = models.CharField(max_length=80)
	time = models.TimeField(blank=False)
	date =  models.DateField(blank=False)
	image_of_area = models.ImageField(upload_to='photos',blank=True)
	post_date = models.DateTimeField(default=timezone.now)
	tools = models.CharField(max_length=60, default=None, null=True)
	work_description = models.TextField(default=None, null=True)

	def __str__(self):
		return self.where


class Post(models.Model):
	GALLERY = 'gallery'
	FUN = 'fun'
	PROJECT = 'project'
	TAGS = ((GALLERY,'Gallery'), (FUN, 'Funs'), (PROJECT, 'project'),(None,'category'))
	title = models.CharField(max_length=60)
	description = models.TextField()
	tag = models.CharField(max_length=20, blank=False, choices=TAGS)
	photo = models.ImageField(upload_to='photos', blank=True)
	post_date = models.DateTimeField(default=timezone.now)
	project_completed = models.BooleanField(blank=True, default=False)
	def __str__(self):
		return self.title

class Event(models.Model):
	title = models.CharField(max_length=90)
	description = models.TextField()
	event_date = models.DateField(default=datetime.now().date())
	event_time = models.TimeField(default=datetime.now().time())
	post_date = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return self.title




a = 'ADDING COMMeNT FOR OPTIONS FOR FUNS'
S = 'IF USeR IS NOT YeT AUTHeNTICATeD SHOW HIM THe COMMeNT BUTTON WHICH IS A LINK ASKING HIM TO AUTHeNTICATeD FIRST'

  
a  = """
comment body 

community works
time
where
date

projects
project title
project body
fundraising 

"""