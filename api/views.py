from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from . models import questions
from . models import profile
from . serializers import questionsCreateSerializer
from . serializers import profileCreateSerializer
from rest_framework import generics



class questionCreateApiView(generics.CreateAPIView):
    serializer_class = questionsCreateSerializer




class questionList(APIView):


	def get(self,request):
		ques= questions.objects.all()
		serializer = questionsCreateSerializer(ques, many=True)
		return Response(serializer.data)


class profileCreateApiView(generics.CreateAPIView):
    serializer_class = profileCreateSerializer

class profileList(APIView):


    def get(self,request):
        pro= profile.objects.all()
        serializer = profileCreateSerializer(pro, many=True)
        return Response(serializer.data)




#     # def post(self):
#     #     pass       
# def post(self,request):
#     ques= questions.objects.all()
#     serializer = questionsSerializer(ques, many=True)
#     return Response(serializer.data)
# # def post(request):
#         posts = questions.objects.all()
#         response_data = {}

#         if request.POST('action') == 'post':
#             question= request.POST('question')
#             courses = request.POST('courses')

#             response_data['question'] = question
#             response_data['courses'] = courses
#             questions.objects.create(
#                 question = question,
#                 courses = courses,
#                 )
#             return JsonResponse(response_data)

#     return render(request, 'create_post.html', {'posts':posts})     


# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import questions
