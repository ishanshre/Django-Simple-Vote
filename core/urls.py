from django.urls import path
from core import views

app_name = "core"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path("<int:question_pk>/results", views.result, name='results'),
    path("<int:question_pk>/vote", views.vote, name='vote'),
]