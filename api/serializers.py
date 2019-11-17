from rest_framework import serializers
#from rest_framework import employees
from . models import questions

class questionsCreateSerializer(serializers.ModelSerializer):
	
	class Meta:
		model= questions
		fields =('question','courses')
		