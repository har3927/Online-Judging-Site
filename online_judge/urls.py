from django.urls import path
from online_judge import views

app_name = 'online_judge'

urlpatterns = [
    path('', views.problems , name = "problems"),
    path('problems/<int:problem_id>/', views.problemDetails, name = "problem_detail"),
    path('problems/<int:problem_id>/submit/', views.submitProblem, name = "submit"),
    path('leaderboard/', views.leaderboard, name = "leaderboard")
]
