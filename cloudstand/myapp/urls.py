from django.urls import path

from .views import (
    TestAPIView,
    HeroSliderAPIView,
    ContactInquiryAPIView
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

        path(
        'contact-inquiry/',
        ContactInquiryAPIView.as_view(),
        name='contact-inquiry'
    ),
]