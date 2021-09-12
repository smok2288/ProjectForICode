from django.urls import path, include
from school.views import StudentView, AllStudenstView, GroupView, AllTeachersView, TeacherView, SubjectView, LessonView, \
    first, student, teacher

app_name = 'school'

urlpatterns = [
    path('', first, name='first'),
    path('1/', student, name='second'),
    path('2/', teacher, name='third'),
    path('students/', AllStudenstView.as_view(), name='students'),
    path('students/<int:pk>/', StudentView.as_view(), name='student_details'),
    path('group/', GroupView.as_view(), name='group'),
    path('teachers/', AllTeachersView.as_view(), name='teachers'),
    path('teachers/<int:pk>/', TeacherView.as_view(), name='teachers_details'),
    path('subject/', SubjectView.as_view(), name='subject'),
    path('lessons/', LessonView.as_view(), name='lessons'),
]
