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
        cursor.execute("select count(*) as totalstaff,position from staff where branchno in (select branchno from branch where address like '%Glasgow%') group by position;")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'branch.html',{
        'q1':data
    })

def branch_query_2(request):
    try:
        cursor.execute('select * from lease where datediff(finish,start) < 365 and propertyno in (select propertyno from property where address like "London%");')
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'branch.html',{
        'q2':data
    })

def branch_query_3(request):
    try:
        cursor.execute("SELECT branchno, SUM(rent) AS total_daily_rental FROM property GROUP BY branchno ORDER BY branchno;")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'branch.html',{
        'q3':data
    })

def branch_query_4(request):
    city = request.GET['bq4_city']
    try:
        cursor.execute(f'select * from branch where address like "%{city}%";')
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'branch.html',{
        'q4':data,
        'input_b4':city
    })

def branch_query_5(request):
    try:
        cursor.execute("SELECT SUBSTRING_INDEX(address, ', ', 1) AS city, COUNT(address) AS num_branches FROM branch GROUP BY city;")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'branch.html',{
        'q5':data
    })

def branch_query_6(request):
    branch_no = request.GET['bq6']
    try:
        cursor.execute(f'select name, position, salary from staff where branchno="{branch_no}" order by name;')
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'branch.html',{
        'q6':data,
        'input_b6':branch_no
    })

def branch_query_7(request):
    branch_no = request.GET['bq7']
    try:
        cursor.execute(f'select staff.staffno,name,count(distinct(propertyno)) as tot_propertirs from staff,property where property.branchno="{branch_no}" and property.branchno=staff.branchno and property.staffno=staff.staffno group by staffno;')
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'branch.html',{
        'q7':data,
        'input_b7':branch_no
    })

def branch_query_8(request):
    input = request.GET['b8']
    try:
        cursor.execute(f'SELECT lease.*, property.address, client.name as client_name, client.phone FROM lease INNER JOIN property ON lease.propertyno = property.propertyno INNER JOIN client ON lease.clientno = client.clientno WHERE lease.branchno = "{input}" AND  finish BETWEEN DATE_ADD(NOW(), INTERVAL 1 MONTH) AND DATE_ADD(NOW(), INTERVAL 2 MONTH);')
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'branch.html',{
        'q8':data,
        'input_b8': input
    })

def client_query_1(request):
    input = request.GET['cq1']
    try:
        cursor.execute(f'select clientno,name,phone,ptype from client where branchno="{input}";')
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'client.html',{
        'q1':data,
        'input_c1':input
    })

def client_query_2(request):
    input = request.GET['c2']
    try:
        cursor.execute(f'select x.name, y.name from client x, staff y where x.staffno=y.staffno and x.branchno="{input}";')
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'client.html',{
        'q2':data,
        'input_c2':input
    })

def client_query_3(request):
    input = request.GET['c3']
    try:
        cursor.execute(f'SELECT * FROM feedback WHERE propertyno = "{input}"')
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'client.html',{
        'q3':data,
        'input_c3':input
    })

def client_query_4(request):
    input = request.GET['c4']
    try:
        cursor.execute(f'SELECT client.name, client.phone FROM client, feedback WHERE client.clientno = feedback.clientno AND feedback.propertyno = "{input}" AND feedback.comment IS NULL;')
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'client.html',{
        'q4':data,
        'input_c4':input
    })

def client_query_5(request):
    input_client = request.GET['c5_1']
    input_property = request.GET['c5_2']
    try:
        cursor.execute(f'SELECT * FROM lease WHERE clientno = "{input_client}" AND propertyno = "{input_property}";')
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'client.html',{
        'q5':data,
        'input_c5_1':input_client,
        'input_c5_2':input_property
    })

def client_query_6(request):
    input_type = request.GET['c6_1']
    input_rent = request.GET['c6_2']
    try:
        cursor.execute(f'SELECT client.clientno, client.name, client.ptype, client.maxrent, client.branchno, client.staffno, client.rdate, client.phone FROM client WHERE client.ptype = "{input_type}" AND client.maxrent <= "{input_rent}";')
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'client.html',{
        'q6':data,
        'input_c6_1':input_type,
        'input_c6_2': input_rent
    })

def manager_query_1(request):
    try:
        cursor.execute("select name,staff.branchno,address,staffno from staff,branch where staffno=managerno  order by address ;")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'manager.html',{
        'q1':data
    })

def owner_query_1(request):
    try:
        cursor.execute("select * from owner where ownerno in (select ownerno from property group by ownerno having count(propertyno)>1);")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'owner.html',{
        'q1':data
    })

def owner_query_2(request):
    input=request.GET['o2']
    try:
        cursor.execute(f'select x.name, x.telephone from owner x, property y where y.propertyno="{input}" and y.ownerno=x.ownerno;')
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'owner.html',{
        'q2':data,
        'input_o2':input
    })

def property_query_1(request):
    try:
        cursor.execute("select propertyno,ptype,address,rent from property where address like '%Glasgow%' order by rent;")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'property.html',{
        'q1':data
    })

def property_query_2(request):
    try:
        cursor.execute("select branchno,count(propertyno) as tot_props from property group by branchno;")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'property.html',{
        'q2':data
    })

def property_query_3(request):
    try:
        cursor.execute("SELECT p.branchno, SUM(p.rent) AS total_daily_rental FROM property p GROUP BY p.branchno ORDER BY p.branchno;")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'property.html',{
        'q3':data
    })

def property_query_4(request):
    try:
        cursor.execute("select * from property where address like 'Glasgow%' and rent<=450;")
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
    input=request.GET['p6']
    try:
        cursor.execute(f'SELECT propertyno, ptype, rooms, address, rent, staff.name AS manager FROM property INNER JOIN staff ON property.staffno = staff.staffno WHERE staff.staffno = "{input}";')
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'property.html',{
        'q6':data,
        'input_p6': input
    })

def property_query_7(request):
    try:
        cursor.execute("select * from property where advertisement>(select avg(advertisement) from property);")
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
    input = request.GET['pq9']
    try:
        cursor.execute(f'select x.* from property x,owner y where x.ownerno=y.ownerno and x.branchno="{input}";')
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'property.html',{
        'q9':data
    })

def property_query_10(request):
    input = request.GET['pq10']
    try:
        cursor.execute(f'select * from property where staffno="{input}";')
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'property.html',{
        'q10':data,
        'input_p10':input
    })

def property_query_11(request):
    try:
        cursor.execute("select * from property where ptype='Flat' and rooms>=3 and address like '%Aberdeen%';")
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'property.html',{
        'q11':data
    })

def staff_query_1(request):
    try:
        cursor.execute("select count(*) as tot_staff,sum(salary) as tot_salary from staff;")
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
    input = request.GET['s3']
    try:
        cursor.execute(f'select name, position, salary from staff where branchno="{input}" order by name;')
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'staff.html',{
        'q3':data,
        'input_s3':input
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
    input_supervisor = request.GET['sq5_1']
    input_branch = request.GET['sq5_2']
    try:
        cursor.execute(f'SELECT s.staffno, s.name, s.sex, s.dob, s.position, s.salary, s.supervisor, s.branchno FROM staff s WHERE s.supervisor = "{input_supervisor}" AND s.branchno = "{input_branch}";')
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'staff.html',{
        'q5':data,
        'input_s5_1':input_supervisor,
        'input_s5_2':input_branch
    })

def staff_query_6(request):
    input = request.GET['sq_6']
    try:
        cursor.execute(f'select * from staff where position="Assistant" and branchno="{input}";')
        data = cursor.fetchall()
    except:
        data = None
    return render(request,'staff.html',{
        'q6':data,
        'input_s6': input
    })