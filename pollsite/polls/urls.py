from django.urls import path, include
from . import views

app_name = "polls"

urlpatterns = [
    path("", views.question_list, name="question_list"),
    path("question/<int:question_id>/", views.question_detail, name="question_detail"),
    path("question/<int:question_id>/vote/", views.vote, name="vote"),
]
