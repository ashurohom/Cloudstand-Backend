from rest_framework.views import APIView
from rest_framework.response import Response

from .models import HeroSlider
from .serializers import HeroSliderSerializer, ContactInquirySerializer


class TestAPIView(APIView):

    def get(self, request):
        return Response({
            "status": True,
            "message": "Hello Ashitosh",
            "data": {
                "name": "Ashitosh",
                "project": "CloudStand"
            }
        })


class HeroSliderAPIView(APIView):

    def get(self, request):

        sliders = HeroSlider.objects.all().order_by('id')

        serializer = HeroSliderSerializer(
            sliders,
            many=True,
            context={'request': request}
        )

        return Response({
            "status": True,
            "message": "Hero Slider Data",
            "data": serializer.data
        })
    


class ContactInquiryAPIView(APIView):

    def post(self, request):

        serializer = ContactInquirySerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response({
                "status": True,
                "message": "Inquiry submitted successfully"
            })

        return Response({
            "status": False,
            "errors": serializer.errors
        }, status=400)    