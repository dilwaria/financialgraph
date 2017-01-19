from django.shortcuts import render

from django.core.urlresolvers import reverse

# from .models import User
# Create your views here.
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
from graphs.models import book1, book2
from django.db.models import Max,Min,Sum
import numpy 

def introduction(request):
	# openpyxl.load_workbook()							
	wb = load_workbook('Book1.xlsx')
	ws1 = wb.get_sheet_by_name("Sheet2")
	print ws1.cell(row=1, column=2).value 
	print ws1.cell(row=1, column=3).value 

	a = book1.objects.first()
	b = book1.objects.last()
	c = book1.objects.all().aggregate(Max('value1'),Max('value2'),Max('value3'),Max('value4'),Max('value5'),Max('value6'),Max('value7'),Max('value8'),Max('value9'),Max('value10'))
	d = book1.objects.all().aggregate(Min('value1'),Min('value2'),Min('value3'),Min('value4'),Min('value5'),Min('value6'),Min('value7'),Min('value8'),Min('value9'),Min('value10'))
	e = book1.objects.all().aggregate(Sum('value1'),Sum('value2'),Sum('value3'),Sum('value4'),Sum('value5'),Sum('value6'),Sum('value7'),Sum('value8'),Sum('value9'),Sum('value10'))
	
	finalarray =[]
	for i in range(1,11):
		print i
		string = "value"+str(i)
		f = book1.objects.values(string)
		emptyarray = []
		for i in f:
			emptyarray.append(i[string])
	
	

		xc = numpy.array(emptyarray)
		yc = numpy.transpose(emptyarray)
		finalarray.append(numpy.dot(xc,yc))

	print finalarray
	GET_CONTEXT = {"firstobs": a,
					"lastobs": b,
					"maximum": c,
					"minimum": d,
					"sum":e,
					"matrix": finalarray}
	# for i in range(2,5002):
		
	# 	x = book2(value1=ws1.cell(row=i, column=2).value,value2=ws1.cell(row=i, column=3).value,value3=ws1.cell(row=i, column=4).value,value4=ws1.cell(row=i, column=5).value,value5=ws1.cell(row=i, column=6).value,value6=ws1.cell(row=i, column=7).value,value7=ws1.cell(row=i, column=8).value,value8=ws1.cell(row=i, column=9).value,value9=ws1.cell(row=i, column=10).value,value10=ws1.cell(row=i, column=11).value  )
	# 	x.save()


	return render(request, 'graphs/introduction.html', GET_CONTEXT)