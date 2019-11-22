from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from . models import questions
from . models import profile
from . models import comment
from . models import tutor
from . serializers import questionsCreateSerializer
from . serializers import profileCreateSerializer
from . serializers import answerCreateSerializer
from . serializers import tutorCreateSerializer
from rest_framework import generics
from django_filters import rest_framework as filters
from django_filters import rest_framework as SearchFilters




class questionCreateApiView(generics.CreateAPIView):
    serializer_class = questionsCreateSerializer

FILTER_REQ_COLUMNS = [field.name for field in questions._meta.get_fields()]
class questionList(generics.ListAPIView):
    queryset = questions.objects.all()
    serializer_class = questionsCreateSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = FILTER_REQ_COLUMNS
       


class profileCreateApiView(generics.CreateAPIView):
    serializer_class = profileCreateSerializer

class profileList(APIView):


    def get(self,request):
        pro= profile.objects.all()
        serializer = profileCreateSerializer(pro, many=True)
        return Response(serializer.data)

class answerCreateApiView(generics.CreateAPIView):
    serializer_class = answerCreateSerializer

class answerList(APIView):
    def get(self,request):
        queryset= comment.objects.all()
        serializer = answerCreateSerializer(queryset, many=True)
        return Response(serializer.data)


class tutorCreateApiView(generics.CreateAPIView):
    queryset= tutor.objects.all()
    serializer_class = tutorCreateSerializer

class tutorList(APIView):
    def get(self,request):
        queryset= tutor.objects.all()
        serializer = tutorCreateSerializer(queryset, many=True)
        return Response(serializer.data)
