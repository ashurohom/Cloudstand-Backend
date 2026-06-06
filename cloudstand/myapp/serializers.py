from rest_framework import serializers
from .models import HeroSlider, ContactInquiry, OpenRole, JobApplication, LiveWebinar, WebinarRegistration, VideoShowcase, TeamCloudStand


class HeroSliderSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()

    class Meta:
        model = HeroSlider
        fields = [
            'id',
            'title',
            'description',
            'image'
        ]

    def get_image(self, obj):

        request = self.context.get('request')

        if obj.image:
            return request.build_absolute_uri(
                obj.image.url
            )

        return None
    


class ContactInquirySerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactInquiry
        fields = [
            'id',
            'name',
            'email',
            'company',
            'phone',
            'service_interested',
            'message'
        ]


class OpenRoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = OpenRole
        fields = [
            'id',
            'title',
            'location',
            'type',
            'experience',
            'summary',

            'key_responsibilities',
            'requirements',
            'preferred',
            'additional_advantage',
            'benefits',

            'created_at'
        ]       


class JobApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobApplication
        fields = [
            'id',
            'role_title',
            'name',
            'email',
            'phone',
            'experience',
            'linkedin_url',
            'cover_note',
            'resume'
        ]


class LiveWebinarSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()

    class Meta:
        model = LiveWebinar
        fields = [
            'title',
            'date',
            'time',
            'speaker',
            'venue',
            'image'
        ]

    def get_image(self, obj):

        request = self.context.get('request')

        if obj.image:
            return request.build_absolute_uri(
                obj.image.url
            )

        return None        
    


class WebinarRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = WebinarRegistration

        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'linkedin_url',
            'webinar_title'
        ]    


class VideoShowcaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoShowcase

        fields = [
            'youtube_url'
        ]        



class TeamCloudStandSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()

    class Meta:
        model = TeamCloudStand
        fields = [
            'id',
            'image',
            'is_hero_image'
        ]

    def get_image(self, obj):

        request = self.context.get('request')

        if obj.image:
            return request.build_absolute_uri(
                obj.image.url
            )

        return None        