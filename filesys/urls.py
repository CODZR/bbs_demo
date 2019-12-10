from django.urls import path
from . import user_views,file_views
urlpatterns = [
    path('user/login', user_views.LoginAPI.as_view()),
    path('user/register', user_views.RegisterAPI.as_view()),
    path('user/detail', user_views.UserDetailAPI.as_view()),

    path('file/detail',file_views.FileDetailAPI.as_view()),
    path('files',file_views.FileQureyAPI.as_view()),

]
