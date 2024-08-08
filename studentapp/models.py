from django.db import models


class Course(models.Model):
    name = models.CharField(max_length = 30)


    def __str__(self):
        return f"{self.name}"

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=13)
    age = models.IntegerField()
    enrollmentdate = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f"{self.name}"


