from django.urls import path
import apps.post.views as views


urlpatterns = [
    path('users/profile/', views.UserProfileView.as_view(), name="user_profile")
    
]
