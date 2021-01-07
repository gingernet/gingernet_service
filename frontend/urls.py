from django.conf.urls import url
from django.urls import path, include
from frontend.views import (
    index, product, solution, research, comp_dyn, partner,
    about, comp_dyn_detail
)

urlpatterns = [
    path('', index, name='index'),
    path(r'research', research, name='research'),
    path(r'comp_dyn', comp_dyn, name='comp_dyn'),
    path(r'partner', partner, name='partner'),
    path(r'about', about, name='about'),
    path(r'product-<int:id>.html', product, name='product'),
    path(r'solution-<int:id>.html', solution, name='solution'),
    path(r'comp_dyn_detail-<int:id>.html', comp_dyn_detail, name='comp_dyn_detail'),
]