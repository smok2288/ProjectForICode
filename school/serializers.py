from pyexpat import model

from rest_framework import serializers

from .models import Student, Group, Teacher, Subject, Lessons


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        depth = 1


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'
        depth = 2


class LessonsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='subject')

    class Meta:
        model = Lessons
        fields = ['id', 'name', 'group']
        depth = 1