from django.http import HttpResponse
from django.shortcuts import render
from businesses.models import Business

def business_list(request):
    return HttpResponse("Business List")

def business_detail(request, pk):
    return HttpResponse(f"Business Detail: {pk}")

def homepage(request):
    business = Business.objects.first()  # ya koi specific business
    return render(request, 'homepage.html', {'business': business})