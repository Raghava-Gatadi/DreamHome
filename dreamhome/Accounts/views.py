from django.shortcuts import render
import mysql.connector

mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="Raghava@7", database="dreamhome")
cursor = mydb.cursor()

def home(request):
    return render(request,'home.html')

def branch(request):
    return render(request,'branch.html')

def client(request):
    return render(request,'client.html')

def manager(request):
    return render(request,'manager.html')

def owner(request):
    return render(request,'owner.html')

def property(request):
    return render(request,'property.html')

def staff(request):
    return render(request,'staff.html')

def branch_query_1(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'branch.html',{
        'q1':data
    })

def branch_query_2(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'branch.html',{
        'q2':data
    })

def branch_query_3(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'branch.html',{
        'q3':data
    })

def branch_query_4(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'branch.html',{
        'q4':data
    })

def branch_query_5(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'branch.html',{
        'q5':data
    })

def branch_query_6(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'branch.html',{
        'q6':data
    })

def branch_query_7(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'branch.html',{
        'q7':data
    })

def branch_query_8(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'branch.html',{
        'q8':data
    })

def client_query_1(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'client.html',{
        'q1':data
    })

def client_query_2(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'client.html',{
        'q2':data
    })

def client_query_3(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'client.html',{
        'q3':data
    })

def client_query_4(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'client.html',{
        'q4':data
    })

def client_query_5(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'client.html',{
        'q5':data
    })

def client_query_6(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'client.html',{
        'q6':data
    })

def manager_query_1(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'manager.html',{
        'q1':data
    })

def owner_query_1(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'owner.html',{
        'q1':data
    })

def owner_query_2(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'owner.html',{
        'q2':data
    })

def property_query_1(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'property.html',{
        'q1':data
    })

def property_query_2(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'property.html',{
        'q2':data
    })

def property_query_3(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'property.html',{
        'q3':data
    })

def property_query_4(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'property.html',{
        'q4':data
    })

def property_query_5(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'property.html',{
        'q5':data
    })

def property_query_6(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'property.html',{
        'q6':data
    })

def property_query_7(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'property.html',{
        'q7':data
    })

def property_query_8(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'property.html',{
        'q8':data
    })

def property_query_9(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'property.html',{
        'q9':data
    })

def property_query_10(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'property.html',{
        'q10':data
    })

def staff_query_1(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'staff.html',{
        'q1':data
    })

def staff_query_2(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'staff.html',{
        'q2':data
    })

def staff_query_3(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'staff.html',{
        'q3':data
    })

def staff_query_4(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'staff.html',{
        'q4':data
    })

def staff_query_5(request):
    try:
        cursor.execute("select * from Branch")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'staff.html',{
        'q5':data
    })