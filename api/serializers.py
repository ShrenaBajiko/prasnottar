from rest_framework import serializers
#from rest_framework import employees
from . models import questions
from . models import comment
from . models import profile
from . models import tutor


class questionsCreateSerializer(serializers.ModelSerializer):
	
	class Meta:
		model= questions
		fields =('__all__')


class profileCreateSerializer(serializers.ModelSerializer):
	
	class Meta:
		model= profile
		fields=('email','username','address') 


class answerCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model=comment
		fields=('__all__')


class tutorCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model=tutor
		fields=('__all__')





		