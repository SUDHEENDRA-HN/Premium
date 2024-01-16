from django.shortcuts import render
from . import ml_pred

def home(request):
    return render(request,'index.html')

def res(request):
    age=int(request.GET['age'])
    sex=int(request.GET['sex'])
    bmi = float(request.GET.get('bmi'))
    children=int(request.GET['children'])
    smoker=int(request.GET['smoker'])
    region=int(request.GET['region'])
    predictions=ml_pred.prediction(age,sex,bmi,children,smoker,region)
    return render(request,'result.html',{'predictions': predictions})
