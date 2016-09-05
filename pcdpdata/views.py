from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def index(request):
    return HttpResponse('<html></html>')

class GetAssessment(APIView):

    def get(self, request):
        return HttpResponse('<html>test</html>')
