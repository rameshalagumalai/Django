from django.shortcuts import render
from .models import Student

def studentsPage(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students.html', context)
