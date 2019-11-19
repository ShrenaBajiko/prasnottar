from rest_framework import serializers
#from rest_framework import employees
from . models import questions
from . models import profile

class questionsCreateSerializer(serializers.ModelSerializer):
	
	class Meta:
		model= questions
		fields =('question','courses')


class profileCreateSerializer(serializers.ModelSerializer):
	
	class Meta:
		model= profile
		fields=('email','username','address') 

		