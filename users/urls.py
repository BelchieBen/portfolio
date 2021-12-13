from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import register

urlpatterns = [
    path('register/', register.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/auth/logout.html'), name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)