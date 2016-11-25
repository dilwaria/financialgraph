from django.shortcuts import render

from django.core.urlresolvers import reverse

# from .models import User
# Create your views here.
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook

def introduction(request):
	# openpyxl.load_workbook()
	wb = load_workbook('D:\\financeproject\\financialgraph\\Book1.xlsx')
	ws1 = wb.get_sheet_by_name("Sheet1")
	print ws1.cell(row=1, column=2).value 
	print ws1.cell(row=1, column=3).value 
	return render(request, 'graphs/introduction.html', {'poll': "p"})