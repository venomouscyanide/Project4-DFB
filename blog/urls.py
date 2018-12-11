from django.urls import path,include
from .views import BlockListView,BlogDetailView,BlogCreateView

urlpatterns=[
	path('',BlockListView.as_view(),name='home'),
	path('post/<int:pk>/',BlogDetailView.as_view(),name='post_detail'),
	path('post/new/',BlogCreateView.as_view(),name='post_new'),
]