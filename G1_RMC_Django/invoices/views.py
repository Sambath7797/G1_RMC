from django.shortcuts import render

# Create your views here.

def Invoices(request):
    return render(request,'invoices/invoices.html')


def add_Invoice(request):
    return render(request,'invoices/add_Invoice.html')