from django.urls import path
from .views import MoviesView, MovieDetailView

urlpatterns = [
    path('', MoviesView.as_view(), name='movies_list'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
]