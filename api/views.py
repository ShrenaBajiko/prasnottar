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
from . serializers import questionsCreateSerializer
from . serializers import profileCreateSerializer
from . serializers import answerCreateSerializer
from rest_framework import generics
from django_filters import rest_framework as filters
from django_filters import rest_framework as SearchFilters




class questionCreateApiView(generics.CreateAPIView):
    serializer_class = questionsCreateSerializer

# class questionList(APIView):
#     def get(self,request):
#         queryset= questions.objects.all()
#         serializer = questionsCreateSerializer(queryset ,many=True)
#         return Response(serializer.data)
#         filter_backends = (SearchFilters,)
#         search_fields = ('courses')


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

    def get(self,request):
        ans= comment.objects.all()
        serializer = answerCreateSerializer(ans, many=True)
        return Response(serializer.data)

# class answerList(generics.ListAPIView):
#     queryset = comment.objects.all()
#     serializer_class = answerCreateSerializer





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
