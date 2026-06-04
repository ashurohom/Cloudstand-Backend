from rest_framework import serializers
from .models import HeroSlider, ContactInquiry, OpenRole, JobApplication, LiveWebinar


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