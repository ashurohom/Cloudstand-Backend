from rest_framework import serializers
from .models import HeroSlider, ContactInquiry


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