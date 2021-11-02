from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MoviesAdminForm(forms.ModelForm):
    descriptions = forms.CharField(label="Opisaniya", widget=CKEditorUploadingWidget())

    class Meta:
        model = Movies
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url']
    list_display_links = ['id', ]


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ['name', 'email']


class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"/>')

    get_image.short_description = "Rasm"


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'poster', 'year', 'country', 'category', 'url', 'draft']
    list_display_links = ['id', ]
    list_filter = ['category', 'year']
    search_fields = ['category__name', 'title', 'year']
    inlines = [MovieShotsInline, ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ['draft']
    actions = ['publish', 'unpublish']
    form = MoviesAdminForm
    readonly_fields = ("get_image",)
    # fields = (('actors', 'directors', 'genres'),)
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"),)
        }),
        (None, {
            "fields": ("descriptions", "poster", "get_image")
        }),
        (None, {
            "fields": ("year", "worl_premiere", "country",)
        }),
        ("Actors", {
            "classes": ("collapse",),
            "fields": (('actors', 'directors', 'genres', 'category'),)
        }),
        (None, {
            "fields": (('budget', 'fees_in_usa', 'fees_in_world'),)
        }),
        ("Options", {
            "fields": (('url', 'draft'),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="50" height="60"/>')

    get_image.short_description = "Poster"

    def unpublish(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 zapis bila obnovleniya"
        else:
            message_bit = f"{row_update} zapis bili obnovleniya"

        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 zapis bila obnovleniya"
        else:
            message_bit = f"{row_update} zapis bili obnovleniya"

        self.message_user(request, f"{message_bit}")

    publish.short_description = "Publikatsiya"
    publish.allowed_permissions = ("change",)

    unpublish.short_description = "Unpublikatsiya"
    unpublish.allowed_permissions = ("change",)


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
    list_display = ['star', 'movie', 'ip']
    # list_display_links = ['id']


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'get_image']
    list_display_links = ['id', ]
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"/>')

    get_image.short_description = "Rasm"


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_image', 'movie']
    list_display_links = ['id', ]
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"/>')

    get_image.short_description = "Rasmlar"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url']
    list_display_links = ['id', ]


admin.sites.site.site_title = "Kinolar"
admin.sites.site.site_header = "Kinolar"
