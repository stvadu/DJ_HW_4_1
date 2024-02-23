from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher

def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    students = Student.objects.order_by(ordering).prefetch_related('teachers')
    context = {'object_list': students}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by



    return render(request, template, context)

def teachers_add(request):
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    for student in students:
        for teacher in teachers:
            student.teachers.add(teacher)
    return HttpResponse('Всем ученикам добавлены учителя')