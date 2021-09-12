from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(max_length=50)
    tel = models.IntegerField(max_length=50)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)

    def __str__(self):
        return self.surname


class Group(models.Model):
    name = models.IntegerField(max_length=3, verbose_name='Номер группы')

    def __str__(self):
        return self.name



class Teacher(models.Model):
    name = models.CharField(max_length=50, verbose_name='Фамилия')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(max_length=50)
    tel = models.IntegerField(max_length=50)

    def __str__(self):
        return self.surname


class Subject(models.Model):
    title = models.CharField(max_length=50, verbose_name='Предмет')
    hours = models.IntegerField(max_length=3, verbose_name='Количество Часов')
    teacher = models.OneToOneField('Teacher', on_delete=models.CASCADE)
    group = models.ManyToManyField('Group', through='Lessons')

    def __str__(self):
        return self.title


class Lessons(models.Model):
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)

    def __str__(self):
        return self.subject
