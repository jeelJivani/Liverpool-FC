from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


 

urlpatterns = [
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('players',views.players,name="players"),
    path('see_ratings/<player_id>',views.see_ratings,name="see_ratings"),
    path('contact',views.contact,name="contact"),
    path('login',views.loginuser,name="loginuser"),
    path('register',views.register,name="register"),
    path('logout',views.logoutuser,name="logout"),
    path('blog',views.blog,name="blog"),
    path('delete_blog/<id>/',views.delete_blog,name="delete_blog"),
    path('update_blog/<id>/',views.update_blog,name="update_blog"),
    path('studentapi/',views.student_api,name="stu_api"),
    path('studentapi/<int:pk>',views.student_api,name="stu_api"),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns ()
