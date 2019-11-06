from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from . models import questions
from . serializers import questionsSerializer


class questionList(APIView):


	def get(self,request):
		ques= questions.objects.all()
		serializer = questionsSerializer(ques, many=True)
		return Response(serializer.data)
	

	def post(self):
		pass	
