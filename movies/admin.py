from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url']
    list_display_links = ['id',]


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ['name', 'email']

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'poster', 'year', 'country', 'category', 'url', 'draft']
    list_display_links = ['id',]
    list_filter = ['category', 'year']
    search_fields = ['category__name', 'title', 'year']
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ['draft']


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'text', 'movie', 'parent']
    list_display_links = ['id', ]
    readonly_fields = ['name', 'email']


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ['id', 'value', ]
    list_display_links = ['id', ]


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip', 'star', 'movie']
    list_display_links = ['id', ]


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'image']
    list_display_links = ['id',]


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'movie']
    list_display_links = ['id',]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url']
    list_display_links = ['id',]
