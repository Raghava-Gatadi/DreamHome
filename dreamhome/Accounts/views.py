from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def owner(request):
    return render(request,'owner.html')

def staff(request):
    return render(request,'staff.html')

def manager(request):
    return render(request,'manager.html')

def property(request):
    return render(request,'property.html')

def branch(request):
    return render(request,'branch.html')

def client(request):
    return render(request,'client.html')