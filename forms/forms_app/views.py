from django.shortcuts import render
from .forms import EmpForm

def displayEmpForm(request):
    if request.method == 'POST':
        empForm = EmpForm(request.POST)
        if empForm.is_valid():
            empForm.save()
    else:
        empForm = EmpForm()
    context = {'empForm': empForm}
    return render(request, 'employeeForm.html', context)
