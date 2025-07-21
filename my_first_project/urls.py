from django.contrib import admin
from django.urls import path, include  # ← Add 'include' if it's not there

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # ← This line connects your app's URLs
]
