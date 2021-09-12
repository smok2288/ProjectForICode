from django.contrib import admin

from school.models import Teacher, Subject, Student, Group, Lessons

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Subject)
admin.site.register(Lessons)
