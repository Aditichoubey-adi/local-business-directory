# myproject/local_business_directory/businesses/models.py

from django.db import models

# Category model (yeh jaisa hai waisa hi rehne dein)
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True) 

    class Meta:
        verbose_name_plural = "Categories" 

    def __str__(self):
        return self.name

# SAARI PURANI BUSINESS MODEL DEFINITIONS KO DELETE KARKE YAHI WALI PASTE KAREIN
class Business(models.Model):
    name = models.CharField(max_length=200)

    # Category field (yeh ab sahi tareeke se hai)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL, # Category delete hone par business ki category NULL ho jaayegi
        null=True,                # Category field NULL ho sakta hai
        blank=True,               # Form mein blank chhod sakte hain
        related_name='businesses' # Category se related businesses ko access karne ke liye
    )

    address = models.CharField(max_length=200) # Maximum length ko 200 par rakha hai, jaisa pehle tha
    # city = models.CharField(max_length=100, default="YourCity") # Agar aapko city field chahiye toh ise uncomment kar dein
    phone = models.CharField(max_length=20, blank=True, null=True) # Phone field ka naam 'phone' hi rakha hai
    # phone_number = models.CharField(max_length=20, blank=True, null=True) # Agar aapko 'phone_number' chahiye toh ise use karein aur 'phone' ko hata dein

    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True) 
    image = models.ImageField(upload_to='business_images/', blank=True, null=True) 
    # created_at = models.DateTimeField(auto_now_add=True) # Agar aapko yeh fields chahiye toh uncomment kar dein
    # updated_at = models.DateTimeField(auto_now=True) # Agar aapko yeh fields chahiye toh uncomment kar dein

    class Meta:
        verbose_name_plural = "Businesses" 

    def __str__(self):
        return self.name