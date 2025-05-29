# myproject/local_business_directory/businesses/forms.py

# myproject/local_business_directory/businesses/forms.py

from django import forms
from .models import Business, Category # <--- Category ko import karein (agar nahi kiya hai to)

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'address', 'phone', 'email', 'website', 'description', 'image', 'category'] # <--- 'category' field yahan add kiya hai
        # Optional: Add Bootstrap classes directly in Meta for better default styling for some fields
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}), # <--- category field ke liye widget add kiya hai
        }