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

# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import questions

# def create_post(request):
#     posts = questions.objects.all()
#     response_data = {}

#     if request.POST.get('action') == 'post':
#         question= request.POST.get('question')
#         courses = request.POST.get('courses')

#         response_data['question'] = question
#         response_data['courses'] = courses

#         questions.objects.create(
#           question = question,
#             courses = courses,
#             )
#         return JsonResponse(response_data)

#     return render(request, 'create_post.html', {'posts':posts})     
