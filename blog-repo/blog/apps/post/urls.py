from django.urls import path
import apps.post.views as views


urlpatterns = [
    path('posts/<slug:slug>/', views.PostDetailView.as_view(), name="post_detail")
    
]
