from django.urls import path

from jobs.api.job_post import (
    PostJobDetailAPIView,
    PostJobListAPIView,
    UserLogin,
    UserRegister,
)


urlpatterns = [
    path("posts/", PostJobListAPIView.as_view()),
    path("posts/<int:pk>/", PostJobDetailAPIView.as_view()),
    path("register/", UserRegister.as_view(), name="user_register"),
    path("login/", UserLogin.as_view(), name="user_login"),
]
