from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>/news_filter', NewsFilter.as_view(), name='news_filter'),
    path('<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('add_news/',  CreateNews.as_view(), name='add_news'),
    path('<int:pk>/add_comment/', CreateComment.as_view(), name='add_comment'),
    path('<int:pk>/edit_news/', EditNews.as_view(), name='edit_news')
]
