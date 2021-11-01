from datetime import date

from django.db import models


# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Kategoriya', max_length=150)
    description = models.TextField("Description")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class Actor(models.Model):
    name = models.CharField('Ism', max_length=150)
    age = models.PositiveSmallIntegerField('Yosh', default=0)
    description = models.TextField('Description')
    image = models.ImageField('Rasm', upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Aktyor va Rejissiyor"
        verbose_name_plural = "Aktyorlar va Rejissiyorlar"


class Genre(models.Model):
    name = models.CharField('Nomi', max_length=100)
    descriptions = models.TextField('Description')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Janr"
        verbose_name_plural = "Janrlar"


class Movies(models.Model):
    title = models.CharField('Title', max_length=100)
    tagline = models.CharField('Tagline', max_length=100, default='')
    descriptions = models.TextField('Description')
    poster = models.ImageField('Poster', upload_to="movies/")
    year = models.PositiveSmallIntegerField('Chiqqan yil', default=2019)
    country = models.CharField('Davlat', max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name='rejissor', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='aktorlar', related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name='janrlar')
    worl_premiere = models.DateField('Dunyoga korsatilgan vaqti', default=date.today)
    budget = models.PositiveIntegerField('Budjet', default=0, help_text="Summani dollarda korsating")
    fees_in_usa = models.PositiveIntegerField('AQSHda tolovlar', default=0, help_text="Summani dollarda korsating")
    fees_in_world = models.PositiveIntegerField('Dunyoda tolovlar', default=0, help_text="Summani dollarda korsating")
    category = models.ForeignKey(Category, verbose_name='Kategoriya', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Chernovek", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Kino"
        verbose_name_plural = "Kinolar"


class MovieShots(models.Model):
    title = models.CharField('Title', max_length=100)
    descriptions = models.TextField('Description')
    image = models.ImageField('Rasm', upload_to="movie_shots/")
    movie = models.ForeignKey(Movies, verbose_name='Kino', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kinodan kadr"
        verbose_name_plural = "Kinodan kadrlar"


class RatingStar(models.Model):
    value = models.SmallIntegerField('Value', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Yulduz reytingi"
        verbose_name_plural = "Yulduzlar reytingi"


class Rating(models.Model):
    ip = models.CharField('IP adress', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='Yulduzcha')
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, verbose_name='Kino')

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Reyting"
        verbose_name_plural = "Reytinglar"


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField('Ism', max_length=100)
    text = models.TextField('Xabar', max_length=5000)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, verbose_name='Kino')
    parent = models.ForeignKey('self', verbose_name='Otasi', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Sharh"
        verbose_name_plural = "Sharhlar"
