from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('register/',views.register, name='register'),
    path('login/',views.loginUser, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('update/',views.update, name='update'),
    path('home/',views.home, name='home'),
    path('post/',views.post, name='post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
