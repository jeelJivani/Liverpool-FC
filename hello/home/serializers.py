from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields= '__all__'

#alternative way

# class StudentSerializer(serializers.Serializer):
#     name= serializers.CharField(max_length=100)
#     roll = serializers.IntegerField()
#     city= serializers.CharField(max_length=100)

#     def create(self, validated_data) :
#         return Student.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         print("before",instance.name)
#         instance.name = validated_data.get('name',instance.name)
#         print("after",instance.name)
#         instance.roll = validated_data.get('roll',instance.roll)
#         instance.city = validated_data.get('city',instance.city )
#         instance.save()
#         return instance
