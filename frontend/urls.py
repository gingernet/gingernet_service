from django.conf.urls import url
from django.urls import path, include
from frontend.views import index, product, solution

urlpatterns = [
    path('', index, name='index'),
    path(r'product-<int:id>.html', product, name='product'),
    path(r'solution-<int:id>.html', solution, name='solution'),
]