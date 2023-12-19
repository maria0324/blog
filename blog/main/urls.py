from django.urls import path
from . import views
from .views import BBLoginView
from .views import BBLogoutView
from django.conf import settings
from django.conf.urls.static import static
from .views import register, edit_profile


urlpatterns = [
                  path('', views.home, name='home'),
                  path('accounts/login/', BBLoginView.as_view(), name='login'),
                  path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
                  path('profile/<int:profile_id>/', views.profile, name='profile'),
                  path('accounts/register/', register, name='register'),
                  path('profile/<int:profile_id>/edit/', edit_profile, name='edit_profile'),
                  path('profile/<int:profile_id>/edit/', views.edit_profile, name='edit_profile'),
                  path('profile/<int:profile_id>/delete/', views.delete_profile, name='delete_profile'),
                  path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
                  path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)