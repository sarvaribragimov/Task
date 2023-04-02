from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Student,Student_information


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()




# Regester
class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(required=True,
                                validators=[UniqueValidator(queryset=Student.objects.all())])
  password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)

  class Meta:
    model = Student
    fields = ('fish', 'password', 'password2',
         'email', 'parent_name', 'city','date','group',)
    extra_kwargs = {
      'fish': {'required': True},
      'parent_name': {'required': True}
    }
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Parol maydonlari mos kelmadi"})
    return attrs
    
  
  def create(self, validated_data):
    password = validated_data.pop('password')
    password2 = validated_data.pop('password2')
    student = Student.objects.create(**validated_data)
    print(student)
    student.set_password(password)
    student.save()
    return student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_information
        fields = "__all__"
        


