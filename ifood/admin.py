from django.contrib import admin

from .models import Suggestion, Promotion, Offer, Category, Restaurant

admin.site.register(Suggestion)
admin.site.register(Promotion)
admin.site.register(Offer)
admin.site.register(Category)
admin.site.register(Restaurant)
