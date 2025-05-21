from django.urls import path
from blog.apps import BlogConfig
from blog.models import Article
from blog.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', ArticleListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', ArticleDetailView.as_view(), name='blog_detail'),
    path('blog/create/', ArticleCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/update', ArticleUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete', ArticleDeleteView.as_view(), name='blog_delete'),
]