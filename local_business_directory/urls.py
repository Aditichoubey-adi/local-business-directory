"""
URL configuration for local_business_directory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# myproject/local_business_directory/myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Media files ke liye
from django.conf.urls.static import static # Media files ke liye

urlpatterns = [
    path('admin/', admin.site.urls),
    path('businesses/', include('businesses.urls')),
    path('', include('businesses.urls')), # <--- Yeh line main root URL ko businesses app ki list par point karegi
    path('accounts/', include('django.contrib.auth.urls')),
]

# Media files serving (if DEBUG is True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)