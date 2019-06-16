from django.db import models
from django.forms import ModelForm
from django.core.validators import FileExtensionValidator

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length = 200)
	text = models.TextField(null=True)
	photo = models.FileField(
		upload_to='uploads/%Y/%m/%d/',
		validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'PNG', 'JPG', 'JPEG'])]
	)
	pub_date = models.DateTimeField('date published', auto_now_add=True, null=True)
	def __str__(self):
		return self.title

class PostModel(ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'text', 'photo']
