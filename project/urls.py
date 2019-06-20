from django.urls import include, path

from . import views

app_name = 'project'
urlpatterns = [
    path('', views.index, name='index'),
	path('<int:post_id>/', views.detail, name='detail'),
	path('create/', views.create, name='create'),
	path('post/', views.post, name='post'),
	path('mypage/', views.mypage, name='mypage'),
	path('register/', views.register, name='register'),
	path('login/', views.login, name='login'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
