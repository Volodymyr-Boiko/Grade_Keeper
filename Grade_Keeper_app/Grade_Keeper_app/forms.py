from django import forms
from Grade_Keeper_app.models import Student, Assignments


class AssigmentForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Assigment name:")
    text = forms.CharField(max_length=1000, help_text='Assigment details:')
    due_date = forms.DateField(help_text='Due date:')
    points_possible = forms.IntegerField(help_text='Max points:')

    class Meta:
        model = Assignments
        fields = ('name', 'text', 'due_date', 'points_possible')


class StudentForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Student name")
    e_mail = forms.EmailField(max_length=128, help_text="E-mail")

    class Meta:
        model = Student
        exclude = ('assignments', 'points')
        fields = ('name', 'e_mail')


class EditStudentForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Student name")
    e_mail = forms.EmailField(max_length=128, help_text="E-mail")
    point = forms.IntegerField(help_text='Points')

    class Meta:
        model = Student
        fields = ('name', 'e_mail', 'point')
