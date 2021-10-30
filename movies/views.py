from django.shortcuts import render
from django.views import View

from movies.models import Movies


class MoviesView(View):
    def get(self, request):
        movies = Movies.objects.all()
        return render(request, "movies/movies.html", {"movie_list": movies})


class MovieDetailView(View):
    def get(self, request, pk):
        movie = Movies.objects.get(id=pk)
        return render(request, "movies/moviesingle.html", {"movie": movie})
