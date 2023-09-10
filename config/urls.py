from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from ifood.views import (
    CategoryViewSet,
    OfferViewSet,
    PromotionViewSet,
    RestaurantViewSet,
    SuggestionViewSet,
)

router = routers.DefaultRouter()
router.register(r"suggestions", SuggestionViewSet)
router.register(r"promotions", PromotionViewSet)
router.register(r"offers", OfferViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"restaurants", RestaurantViewSet)




urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
