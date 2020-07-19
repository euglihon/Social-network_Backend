from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    # реализация логирования через Django auth
    path('', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
