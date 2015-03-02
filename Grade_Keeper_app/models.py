from django.db import models

class Assignments(models.Model):
    assigment_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    text = models.CharField(max_length=1000)
    due_date = models.DateField()
    points_possible = models.IntegerField(default=0)


class Student(models.Model):
    assignments = models.ForeignKey(Assignments)
    student_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40, unique=True)
    e_mail = models.EmailField(max_length=30)
    point = models.IntegerField(default=0)

    # method
    def grade_point(self, assignment_id):
        assignment = Assignments.objects.get(int(assignment_id))
        grade = (float(self.point) / float(assignment.points_possible)) * 100.0
        return grade
