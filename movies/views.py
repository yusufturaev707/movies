from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from  .forms import ReviewForm

from movies.models import Movies


class MoviesView(ListView):
    model = Movies
    queryset = Movies.objects.filter(draft=False)
    template_name = "movies/movies.html"


class MovieDetailView(DetailView):
    model = Movies
    slug_field = "url"
    template_name = "movies/movie_detail.html"


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movies.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
