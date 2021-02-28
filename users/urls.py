from django.contrib.auth import views as auth_views
from django.urls import include, path

from users import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='registration/logout.html'), name='logout'),
    path('', include('django.contrib.auth.urls')),
]
