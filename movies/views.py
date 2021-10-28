from django.shortcuts import render
from django.views import View

from movies.models import Movies


class MoviesView(View):
    def get(self, request):
        movies = Movies.objects.all()
        return render(request, "movies/movie_list.html", {"movie_list": movies})
