from django.contrib import admin
from django.urls import path, include
import firstapp.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', firstapp.views.main, name="main"),
    path('accounts/', include('accounts.urls')),
]
