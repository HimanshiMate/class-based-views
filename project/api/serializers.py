from rest_framework import serializers
from .models import Student


# class StudentSerializer(serializers.Serializer):
#     stu_name=serializers.CharField(max_length=50)
#     stu_city=serializers.CharField(max_length=50)
#     stu_contact=serializers.IntegerField()

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"