from django.shortcuts import render,redirect

from django.core.urlresolvers import reverse

# from .models import User
# Create your views here.
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
from graphs.models import book1, book2, book3, book4
from django.db.models import Max,Min,Sum
import numpy 

# importing forms 
from graphs.forms import PostInputForm

def introduction(request,variable_id=1):
	# openpyxl.load_workbook()							
	wb = load_workbook('Book1.xlsx')
	ws1 = wb.get_sheet_by_name("Sheet4")
	print ws1.cell(row=1, column=2).value 
	print ws1.cell(row=1, column=3).value

	print variable_id
	if variable_id=="1": 
		print "here"
		book = book1
	elif variable_id=="2":
		book =book2
	elif variable_id=="3":
		book=book3
	elif variable_id=="4":
		book = book4


	a = book.objects.first()
	b = book.objects.last()
	c = book.objects.all().aggregate(Max('value1'),Max('value2'),Max('value3'),Max('value4'),Max('value5'),Max('value6'),Max('value7'),Max('value8'),Max('value9'),Max('value10'))
	d = book.objects.all().aggregate(Min('value1'),Min('value2'),Min('value3'),Min('value4'),Min('value5'),Min('value6'),Min('value7'),Min('value8'),Min('value9'),Min('value10'))
	e = book.objects.all().aggregate(Sum('value1'),Sum('value2'),Sum('value3'),Sum('value4'),Sum('value5'),Sum('value6'),Sum('value7'),Sum('value8'),Sum('value9'),Sum('value10'))
	
	finalarray =[]
	for i in range(1,11):
		print i
		string = "value"+str(i)
		f = book.objects.values(string)
		emptyarray = []
		for i in f:
			emptyarray.append(i[string])
	
	

		xc = numpy.array(emptyarray)
		yc = numpy.transpose(emptyarray)
		finalarray.append(numpy.dot(xc,yc))

	print finalarray

	if request.method == "POST":
		form = PostInputForm(request.POST)
		if form.is_valid():
			post = form.save()
			post.save()
			return redirect('introduction',variable_id)	


	else:
		form = PostInputForm()

	GET_CONTEXT = {"firstobs": a,
					"lastobs": b,
					"maximum": c,
					"minimum": d,
					"sum":e,
					"matrix": finalarray,
					"form": form}
	

	return render(request, 'graphs/introduction.html', GET_CONTEXT)



def insertDataFunction():
	for i in range(2,5002):
		
		x = book4(value1=ws1.cell(row=i, column=2).value,value2=ws1.cell(row=i, column=3).value,value3=ws1.cell(row=i, column=4).value,value4=ws1.cell(row=i, column=5).value,value5=ws1.cell(row=i, column=6).value,value6=ws1.cell(row=i, column=7).value,value7=ws1.cell(row=i, column=8).value,value8=ws1.cell(row=i, column=9).value,value9=ws1.cell(row=i, column=10).value,value10=ws1.cell(row=i, column=11).value  )
		x.save()
 


def graphing(request):
	GET_CONTEXT = {}
	return render(request, 'graphs/graphing.html', GET_CONTEXT)