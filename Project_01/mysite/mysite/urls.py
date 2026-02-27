
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),  #already added by default
    path('blog/',include('blog.urls',namespace='blog')),  # inside application(blog) folder
]