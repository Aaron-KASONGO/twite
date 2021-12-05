from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('log-in/', views.Login.as_view(), name="login"),
    path("log-out/", views.Logout.as_view(), name="logout"),
    path('signup/', views.signUp, name='sign_up'),
    path("create-post/", views.to_post, name="post"),
    path("update-profile/", views.update_profile, name="update_profile")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
