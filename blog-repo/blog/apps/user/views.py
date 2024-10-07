from django.views.generic import TemplateView

class UserProfileView(TemplateView):
    template_name = 'users/user_profile.html'

# Create your views here.
