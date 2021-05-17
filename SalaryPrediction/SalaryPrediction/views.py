from django.shortcuts import render
import joblib

def home(request):
    return render(request, "home.html")

def result(request):

    model = joblib.load('Final.sav')
    lis = []
    lis.append(request.GET['Age'])
    lis.append(request.GET['Rating'])
    lis.append(request.GET['python'])
    lis.append(request.GET['spark'])
    lis.append(request.GET['aws'])
    lis.append(request.GET['seniority'])
    lis.append(request.GET['excel'])
    lis.append(request.GET['job_state'])
    lis.append(request.GET['hourly'])
    lis.append(request.GET['job_simp'])
    lis.append(request.GET['Sector'])
    lis.append(request.GET['Type of ownership'])
    lis.append(request.GET['Industry'])
    prediction = model.predict([lis])
    return render(request, "result.html", {'prediction': prediction})