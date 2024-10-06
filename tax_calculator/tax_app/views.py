from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def defult_view(request):
   return HttpResponse("<h1>this is a site to claculate tax<h1>")


def calculate_tax(request , number):
   tax_rate=0.15
   total_price = number+(number *tax_rate)
   return HttpResponse(f"<h1> total price after 15% tax<h1>")

def show_tax_rate(request):
   tax_rate=0.15
   return HttpResponse