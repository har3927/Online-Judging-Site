from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('problemset/', views.list_problems, name = "list_problems"),
    path('problemset/problem/<int:question_id>/', views.detail, name = 'detail'),
    path('leaderboard/', views.leaderboard, name = 'leaderboard')
]
