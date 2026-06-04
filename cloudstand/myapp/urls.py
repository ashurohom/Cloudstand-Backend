from django.urls import path

from .views import (
    TestAPIView,
    HeroSliderAPIView
)

urlpatterns = [

    path(
        'test/',
        TestAPIView.as_view(),
        name='test-api'
    ),

    path(
        'hero-slider/',
        HeroSliderAPIView.as_view(),
        name='hero-slider'
    ),
]