from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from school.models import Student, Group, Teacher, Subject, Lessons
from school.serializers import StudentSerializer, GroupSerializer, TeacherSerializer, SubjectSerializer, \
    LessonsSerializer


class AllStudenstView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GroupView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class AllTeachersView(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherView(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class SubjectView(ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class LessonView(ListAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


def first(request):
    return render(request, 'first.html')


def student(request):
    return render(request, 'student.html')


def teacher(request):
    return render(request, 'teacher.html')
