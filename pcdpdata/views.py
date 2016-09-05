from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# App code
from .models import Assessment
from .serializers import AssessmentSerializer

class AssessmentList(APIView):

    def get(self, request):
        assessment = get_object_or_404(Assessment.objects.all())
        serializer = AssessmentSerializer(assessment, many=True)
        return Response(serializer)

class AssessmentDetail(APIView):

    def get(self, request, assessment_id):
        assessment = get_object_or_404(Assessment.objects.filter(pk=assessment_id))
        serializer = AssessmentSerializer(assessment)
        return Response(serializer.data)

