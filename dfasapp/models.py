from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Student_Info(models.Model):
    programme  = models.CharField(max_length=100,null=True)
    surnName  = models.CharField(max_length=100,null=True)
    firstname = models.CharField(max_length=100,null=True)
    lastname  = models.CharField(max_length=100,null=True)
    sex  = models.CharField(max_length=100,null=True)

    state= models.CharField(max_length=100,null=True)
    local_goverment_area= models.CharField(max_length=100,null=True)
    address= models.CharField(max_length=100,null=True)
    date_of_birth= models.CharField(max_length=100,null=True)
    date_of_Resumption= models.CharField(max_length=100,null=True)
    marital_status = models.CharField(max_length=100,null=True)
    department= models.CharField(max_length=100,null=True)
    religion= models.CharField(max_length=100,null=True)
    olevel_number_of_sittings= models.CharField(max_length=100,null=True)
    student_num= models.CharField(max_length=100)
    fathers_num= models.CharField(max_length=100,null=True)
    mothers_num= models.CharField(max_length=100,null=True)
    sub_comb_1= models.CharField(max_length=100,null=True)
    sub_comb_2= models.CharField(max_length=100,null=True)
    sub_comb_3= models.CharField(max_length=100,null=True)
    first_choice= models.CharField(max_length=100,null=True)
    first_choice_course=models.CharField(max_length=100,null=True)
    second_choice= models.CharField(max_length=100,null=True)
    second_choice_course= models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    father_occupation = models.CharField(max_length=100,null=True)
    mother_occupation = models.CharField(max_length=100,null=True)


    def __str__(self):
        return self.firstname

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    body = models.CharField(max_length=100)

