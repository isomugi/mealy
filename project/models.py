from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User


class Post(models.Model):
	title = models.CharField(max_length = 200)
	text = models.TextField(null=True)
	photo = models.FileField(
		upload_to='uploads/%Y/%m/%d/',
		validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'PNG', 'JPG', 'JPEG'])]
	)
	like_num = models.IntegerField(default = 0)
	pub_date = models.DateTimeField('date published', auto_now_add=True, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.title


class PostModel(ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'text', 'photo']

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.name
