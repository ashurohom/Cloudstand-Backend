from django.contrib import admin
from .models import HeroSlider, ContactInquiry, OpenRole, JobApplication, LiveWebinar, WebinarRegistration


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


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'role_title',
        'email',
        'experience',
        'status',
        'applied_at'
    )

    list_filter = (
        'status',
        'applied_at'
    )

    search_fields = (
        'name',
        'email',
        'role_title'
    )

    list_editable = (
        'status',
    )

    readonly_fields = (
        'applied_at',
    )  


@admin.register(LiveWebinar)
class LiveWebinarAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'speaker',
        'date',
        'time',
        'venue',
        'is_active'
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'speaker',
        'venue'
    )      


@admin.register(
    WebinarRegistration
)
class WebinarRegistrationAdmin(
    admin.ModelAdmin
):

    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'webinar_title',
        'registration_status',
        'registered_at'
    )

    search_fields = (
        'first_name',
        'last_name',
        'email',
        'webinar_title'
    )

    list_filter = (
        'registration_status',
        'registered_at'
    )

    list_editable = (
        'registration_status',
    )

    readonly_fields = (
        'registered_at',
    )