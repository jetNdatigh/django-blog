from django.urls import path
from . import views as blog_views
from . views import (
	PostListView,
	UserPostListView,
	PostDetailView, 
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	PostAuthorView
	)

urlpatterns = [
    # path('', blog_views.home, name = 'blog-home'),
    path('', PostListView.as_view(), name = 'blog-home'),

    path('<str:username>/posts/', UserPostListView.as_view(), name = 'user-posts'),

    path('post/<int:pk>/author/', PostAuthorView.as_view(), name = 'post-author'),
    # path('post/<int:pk>/author/', blog_views.author_profile, name = 'post-author'),

    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),

    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('about/', blog_views.about, name = 'blog-about')

]