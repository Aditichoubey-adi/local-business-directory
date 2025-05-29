# myproject/local_business_directory/businesses/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Business, Category
from .form import BusinessForm # Corrected from .form to .forms
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required


def business_list(request):
    query = request.GET.get('q') # Search query
    category_id = request.GET.get('category') # Category filter parameter

    businesses = Business.objects.all()

    if query:
        businesses = businesses.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(address__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query)
        ).distinct()

    # Category filter logic
    if category_id:
        businesses = businesses.filter(category__id=category_id)

    # Optional: Order businesses
    businesses = businesses.order_by('name')

    # Pagination Logic
    paginator = Paginator(businesses, 9) # Har page par 9 businesses dikhayenge
    page_number = request.GET.get('page') # URL se 'page' parameter lega

    try:
        page_obj = paginator.get_page(page_number)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    except Exception: # General exception for robustness
        page_obj = paginator.get_page(1)

    categories = Category.objects.all().order_by('name')

    context = {
        'businesses': page_obj, # Ab 'businesses' mein sirf current page ke items hain
        'query': query,
        'categories': categories,
        'selected_category_id': category_id,
        'page_obj': page_obj,
    }
    return render(request, 'businesses/business_list.html', context)


def business_detail(request, pk):
    business = get_object_or_404(Business, pk=pk)
    context = {
        'business': business,
        'title': business.name
    }
    return render(request, 'businesses/business_detail.html', context)


@login_required # Login required for adding a business
def add_business(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('businesses:list') # Redirect to business list after adding
    else:
        form = BusinessForm()
    return render(request, 'businesses/add_business.html', {'form': form}) # Corrected template name


@login_required # Login required for editing a business
def edit_business(request, pk):
    business = get_object_or_404(Business, pk=pk)
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES, instance=business)
        if form.is_valid():
            form.save()
            return redirect('businesses:detail', pk=business.pk) # Redirect to business detail after editing
    else:
        form = BusinessForm(instance=business)
    return render(request, 'businesses/edit_business.html', {'form': form, 'business': business}) # Pass business object to context


@login_required # Login required for deleting a business
def delete_business(request, pk):
    business = get_object_or_404(Business, pk=pk)
    if request.method == 'POST':
        business.delete()
        return redirect('businesses:list') # Redirect to business list after deleting
    return render(request, 'businesses/confirm_delete.html', {'business': business}) # Corrected template name


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('businesses:list') # <--- HERE IS THE MAIN FIX! Redirect to business list after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})