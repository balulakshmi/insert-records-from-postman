from django.db import models
class CourseModel(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    fee = models.FloatField()

class CommonModel(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    contactno = models.IntegerField()
    subject = models.CharField(max_length=50)
    class Meta:
        abstract=True
class FacultyModel(CommonModel):
    subject = models.ManyToManyField(CourseModel)
    salary=models.FloatField()
class StudentModel(CommonModel):
    subject = models.ManyToManyField(CourseModel)
    fee = models.FloatField()