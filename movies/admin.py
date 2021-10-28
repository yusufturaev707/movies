from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Movies)
admin.site.register(Reviews)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Actor)
admin.site.register(Movie_shots)
admin.site.register(Genre)