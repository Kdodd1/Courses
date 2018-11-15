from __future__ import unicode_literals
from django.db import models
import re

class CourseManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['name']) < 5:
			errors['name'] = "*Course name must be at least 6 chracters long"

		if len(postData['description']) < 15:
			errors['description'] = "*Description must be at least 16 characters long"
		return errors
class Course(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	objects = CourseManager()

class Description(models.Model):
	description = models.TextField()
	courseDesc = models.OneToOneField(Course)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	objects = CourseManager()
