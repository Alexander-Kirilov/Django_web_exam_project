from django.urls import path

from .views import (
    NewsAllListView,
    NewsDetailView,
    NewsCreateView,
    NewsUpdateView,
    NewsDeleteView,
)

urlpatterns = [
    path('', NewsAllListView.as_view(), name='news_list_all'),
    path('create/', NewsCreateView.as_view(), name='news_create'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_details'),
    path('<int:pk>/update/', NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
]

