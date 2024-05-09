from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.models import User		#16-04-2024
from django.contrib.auth import login as auth_login,logout,authenticate		#16-04-2024 after making changes in the register.html

from .models import *

from .models import Invoice

# Create your views here.

def home(request):
	return render(request,"home.html")


def register(request):
	
	if (request.method == "POST"):		
		first_name = request.POST.get("fname")
		last_name = request.POST.get("lname")
		email_ID = request.POST.get("email")
		password = request.POST.get("pass")

		user = User.objects.create_user(username=email_ID, email=email_ID, first_name = first_name, last_name = last_name, password=password)

		return render(request,"login.html", {"message":"Successfully registered now try to log in"})
	
	return render(request,"register.html")	


def login(request):

	if(request.method == "POST"):
		username = request.POST.get("username")
		password = request.POST.get("pass")

		user = authenticate(username = username, password = password)

		print(user)
		if user:
			auth_login(request, user)
		
		return render(request, "invoice5.html", {"message":"You are logged in"})
	

	return render(request,"login.html")

# def create_invoice(request):

# 	if request.method == 'POST':
# 		invoice_date = request.POST.get("invoice_date")
# 		invoice_number = request.POST.get("invoice_number")
# 		name = request.POST.get("customer_name")
# 		due_date = request.POST.get("due_date")

# 		counter = request.POST.get("count")

# 		for i in range(int(counter)): #(0,1,2,3,4,5)
# 			product_name = request.POST.get("product_name" +  str(i + 1))
# 			qty = request.POST.get("qty" +  str(i + 1))
# 			rate = request.POST.get("rate" +  str(i + 1))
# 			total = request.POST.get("total" +  str(i + 1))
			
# 			Invoice.objects.create(
# 				invoice_date = invoice_date,
# 				invoice_number = invoice_number,
# 				name = name, 
# 				due_date =  due_date,

# 				product =  product_name, 
# 				qty1 = qty,
# 				rate1 =  rate, 
# 				total1 = total, 
# 				user = request.user)
			


# 			# invoice_date(from html) = invoice_date(from models.py of Invoice)

# 	return render(request,"invoice5.html")


# def create_invoice(request):

# 	if request.method == 'POST':
# 		invoice_date = request.POST.get("invoice_date")
# 		invoice_number = request.POST.get("invoice_number")
# 		name = request.POST.get("customer_name")
# 		due_date = request.POST.get("due_date")

# 		counter = request.POST.get("count")

# 		Invoice.objects.create(
# 				invoice_date = invoice_date,
# 				invoice_number = invoice_number,
# 				name = name, 
# 				due_date =  due_date,
# 				)

# 				# product =  product_name, 
# 				# qty1 = qty,
# 				# rate1 =  rate, 
# 				# total1 = total, 
# 				# user = request.user)

# 		for i in range(int(1,counter+1)): #(0,1,2,3,4,5)
# 			product_name = request.POST.get("product_name" +  str(i + 1))
# 			qty = request.POST.get("qty" +  str(i + 1))
# 			rate = request.POST.get("rate" +  str(i + 1))
# 			total = request.POST.get("total" +  str(i + 1))
			
# 			Product.objects.create(
# 				product = product_name,
# 				qty1 = qty,
# 				rate1 = rate, 
# 				total1 =  total,
# 				)
			
			


# 			# invoice_date(from html) = invoice_date(from models.py of Invoice)

# 	return render(request,"invoice5.html")

def create_invoice(request):

	if request.method == 'POST':
		invoice_date = request.POST.get("invoice_date")
		invoice_number = request.POST.get("invoice_number")
		name = request.POST.get("customer_name")
		due_date = request.POST.get("due_date")

		counter = request.POST.get("count")

		for i in range(int(counter)): #(0,1,2,3,4,5)
			product_name1 = request.POST.get("product_name" +  str(i + 1))
			qty = request.POST.get("qty" +  str(i + 1))
			rate = request.POST.get("rate" +  str(i + 1))
			total = request.POST.get("total" +  str(i + 1))
			
			Invoice.objects.create(
				invoice_date = invoice_date,
				invoice_number = invoice_number,
				name = name, 
				due_date =  due_date,

				product_name1 =  product_name1, 
				qty1 = qty,
				rate1 =  rate, 
				total1 = total, 
				user = request.user)
			


			# invoice_date(from html) = invoice_date(from models.py of Invoice)

	return render(request,"invoice5.html")

#06-5-2024

def viewinvoice(request):
	invoices=Invoice.objects.all() #without any condition, fetch all data.
	# invoice.objects.filter() need to write argument ex:- Invoice = 123  or cust_name = 'name'.
	context={'invoice1':invoices}
	return render(request,"viewinvoice.html",context)
 
def deleteinvoice(request,pk):
	Invoice.objects.filter(id=pk).delete()
	invoices = Invoice.objects.all()
	context = {'invoice1':invoices}
	# print(invoices.first())

	return render(request,"viewinvoice.html",context)