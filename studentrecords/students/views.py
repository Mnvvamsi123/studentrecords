from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'students/student_form.html', {'form': form})

def student_update(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'students/student_form.html', {'form': form})

def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})
