from django.contrib import admin
from .models import HeroSlider, ContactInquiry, OpenRole


@admin.register(HeroSlider)
class HeroSliderAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'created_at'
    )

    search_fields = (
        'title',
    )




@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'email',
        'phone',
        'service_interested',
        'is_contacted',
        'created_at'
    )

    search_fields = (
        'name',
        'email',
        'phone'
    )

    list_filter = (
        'is_contacted',
        'created_at'
    )    




@admin.register(OpenRole)
class OpenRoleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'location',
        'type',
        'experience',
        'is_active',
        'created_at'
    )

    list_filter = (
        'is_active',
        'type'
    )

    search_fields = (
        'title',
        'location',
        'experience'
    )    