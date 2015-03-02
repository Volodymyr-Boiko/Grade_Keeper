from django.shortcuts import render, redirect, get_object_or_404
from Grade_Keeper_app.models import Assignments, Student
from Grade_Keeper_app.forms import StudentForm, AssigmentForm, EditStudentForm


def main_assignments(request):
    context = {}
    try:
        assignments = Assignments.objects.all()
        students = Student.objects.all()
        context['students'] = students
        context['assignments'] = assignments
    except Assignments.DoesNotExist:
        pass
    return render(request, 'main_assignments.html', context)


def assignments(request, assign_id):
    context = {}
    try:
        assignment = get_object_or_404(Assignments, pk=int(assign_id))
        students = Student.objects.filter(assignments=assignment)

        context['assignment'] = assignment
        context['students'] = students
    except Assignments.DoesNotExist, Student.DoesNotExist:
        return redirect('/grade_keeper/')
    return render(request, 'students.html', context)


def add_assigment(request):
    if request.method == 'POST':
        form = AssigmentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/grade_keeper/')
        else:
            print form.errors
    else:
        form = AssigmentForm()
    return render(request, 'add_assigment.html', {'form': form})


def delete(request):
    student = Student.objects.all()
    assigment = Assignments.objects.all()
    student.delete()
    assigment.delete()
    return redirect('/grade_keeper/')


def edit_student(request, st_id, assign_id):
    student = get_object_or_404(Student, pk=int(st_id))
    assignment = get_object_or_404(Assignments, pk=int(assign_id))
    if request.method == "POST":
        form = EditStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save(commit=True)
            # return redirect('/grade_keeper/')
            return assignments(request, assign_id)
    else:
        form = EditStudentForm(instance=student)
        return render(request, 'edit_student.html', {'form': form, 'assignment_id': assignment.assigment_id })

def add_student(request, assign_id):
    context = {}
    assign = Assignments.objects.get(pk=int(assign_id))
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            if assign:
                student = form.save(commit=False)
                student.assignments = assign
                student.save()
                return assignments(request, assign_id)
            else:
                print form.errors
    else:
        form = StudentForm
    context['form'] = form
    context['assignments'] = assign
    context['assignment_id'] = assign.assigment_id
    return render(request, 'add_student.html', context)
