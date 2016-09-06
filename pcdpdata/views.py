from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# App code
from .models import Assessment, Choice, Question, User
from .serializers import AssessmentSerializer, UserSerializer

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

class ResultList(APIView):

    def get(self, request, assessment_id):
        questions = Question.objects.filter(assessment_id=assessment_id)
        choices = Choice.objects.filter(question_id__in=questions.values('id'))
        users_who_took_the_assessment = User.objects.filter(answers__in=choices.values('id')).distinct()
        serializer = UserSerializer(users_who_took_the_assessment, many=True)
        return Response(serializer.data)

class UserResult(APIView):
    def get(self, request, assessment_id, user_id):
        questions = Question.objects.filter(assessment_id=assessment_id)
        choices = Choice.objects.filter(question_id__in=questions.values('id'))
        users_who_took_the_assessment = User.objects.get(answers__in=choices.values('id'), id=user_id)
        serializer = UserSerializer(users_who_took_the_assessment)
        return Response(serializer.data)

    
