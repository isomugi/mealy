from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length = 200)
	text = models.TextField()
	photo = models.CharField(max_length = 255)
	pub_date = models.DateTimeField('date published', auto_now_add=True, null=True)
	def __str__(self):
		return self.text
