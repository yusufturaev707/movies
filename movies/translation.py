from modeltranslation.translator import register, TranslationOptions
from .models import Category, Actor, Movies, Genre, MovieShots


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name", "description")


@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ("name", "description")


@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ("name", "descriptions")


@register(Movies)
class MoviesTranslationOptions(TranslationOptions):
    fields = ("title", "tagline", "descriptions", "country")


@register(MovieShots)
class MovieShotsTranslationOptions(TranslationOptions):
    fields = ("title", "descriptions",)
