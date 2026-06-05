from rest_framework.parsers import (
    MultiPartParser,
    FormParser
)

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import HeroSlider, OpenRole, LiveWebinar, WebinarRegistration
from .serializers import HeroSliderSerializer, ContactInquirySerializer, OpenRoleSerializer, JobApplicationSerializer, LiveWebinarSerializer, WebinarRegistrationSerializer


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
    


class OpenRoleAPIView(APIView):

    def get(self, request):

        roles = OpenRole.objects.filter(
            is_active=True
        )

        serializer = OpenRoleSerializer(
            roles,
            many=True
        )

        return Response(serializer.data)    
    

class ApplyRoleAPIView(APIView):

    parser_classes = (
        MultiPartParser,
        FormParser
    )

    def post(self, request):

        serializer = JobApplicationSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                {
                    "status": True,
                    "message": "Application submitted successfully"
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            {
                "status": False,
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )    
    

class LiveWebinarAPIView(APIView):

    def get(self, request):

        webinar = LiveWebinar.objects.filter(
            is_active=True
        ).order_by('-id').first()

        if not webinar:
            return Response({})

        serializer = LiveWebinarSerializer(
            webinar,
            context={'request': request}
        )

        return Response(serializer.data)



class WebinarRegistrationAPIView(APIView):

    def post(self, request):

        email = request.data.get('email')
        webinar_title = request.data.get('webinar_title')

        already_registered = WebinarRegistration.objects.filter(
            email=email,
            webinar_title=webinar_title
        ).exists()

        if already_registered:

            return Response(
                {
                    "status": False,
                    "message": "You have already registered for this webinar."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = WebinarRegistrationSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                {
                    "status": True,
                    "message": "Registration Successful"
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            {
                "status": False,
                "message": "Invalid data submitted.",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )