from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Student_Info,Message

# Create your views here.

@csrf_exempt
def register(request):
    if request.method == "POST":
       formData = request.body
       formData = json.loads(formData.decode('utf-8'))
       data = json.loads(formData) 
       programme = data.get("Alevel")
       surname = data.get("surname")
       firstname = data.get("firstname")
       lastname = data.get("lastname")
       gender = data.get("gender")
       state = data.get("state")
       local_government_area = data.get("lga")
       address = data.get('Haddress')
       email_address = data.get("email")
       Department = data.get("course")
       religion = data.get("religion")
       olevel = data.get("ol")
       student_phone_number = data.get("sphone")
       father_phone_number = data.get("pphone")
       mothers_num= data.get("mother")
       subject1 = data.get("subject1")
       subject2 = data.get("subject2")
       subject3 = data.get("subject3")
       firstchoice = data.get("fchoice")
       course = data.get("fcourse")
       marital_status= data.get("marital")
       date_of_birth =data.get("DOB")
       date_of_Resumption=data.get("resumption")
       secondchoice = data.get("schoice")
       course2 = data.get("scourse")
       father_occupation = data.get("fwork")
       mother_occupation = data.get("mwork")
       Student_Info.objects.create(programme=programme,surnName=surname,firstname=firstname,lastname=lastname,
                                   sex=gender, local_goverment_area=local_government_area
                                   ,department=Department,state=state, religion=religion, olevel_number_of_sittings=olevel,student_num=student_phone_number, fathers_num=father_phone_number,
                                   sub_comb_1=subject1, sub_comb_2=subject2,sub_comb_3=subject3,first_choice=firstchoice,first_choice_course=course, second_choice=secondchoice, second_choice_course=course2, email=email_address,father_occupation=father_occupation,
                                   mother_occupation=mother_occupation,address=address,marital_status=marital_status,date_of_birth=date_of_birth,date_of_Resumption=date_of_Resumption,mothers_num=mothers_num)
       return JsonResponse({"status":"200 ok","message":"saved sucessfully"})

    return JsonResponse({"error":"postrequest"})

@csrf_exempt
def home(request):
    if request.method == "POST":
        formData = request.body
        formData = json.loads(formData.decode('utf-8'))
        data = json.loads(formData)
        name=data.get("names")
        email=data.get("ema")
        body=data.get("body")
        print(name+""+ ""+email+""+body)

        Message.objects.create(name=name,email=email,body=body)
        return JsonResponse({"success":"Message sent sucessful"})

    return JsonResponse({"error":"Invalid  request"})


@csrf_exempt
def login(request): 
    if request.method == "POST":
      return JsonResponse({"error":"Invalid  Passowrd"})
