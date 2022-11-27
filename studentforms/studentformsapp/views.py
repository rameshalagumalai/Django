from django.shortcuts import render, redirect
from .forms import StudentForm

def addStudentData(request):
    if request.method == 'POST':
        student = StudentForm(request.POST)
        if student.is_valid():
            try:
                print(request)
                return redirect('/admin')
            except:
                pass    
    else:
        student = StudentForm()
    context = {'form': student}
    return render(request, 'studentform.html', context)  
