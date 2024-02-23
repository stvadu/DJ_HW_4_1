from django.urls import path

from school.views import students_list, teachers_add

urlpatterns = [
    path('', students_list, name='students'),
    path('add_teachers', teachers_add, name='add')
]