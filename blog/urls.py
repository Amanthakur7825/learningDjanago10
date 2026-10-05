from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog/', views.blog, name='blog_page'),
]
