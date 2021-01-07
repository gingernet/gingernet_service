#encoding=utf-8

import uuid
import time
import logging
from typing import Dict, Any
from functools import wraps
from decimal import Decimal
from django.core.cache import cache
from django.core import serializers
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpRequest, JsonResponse, Http404
from django.conf import settings
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from common.helpers import paged_items, ok_json, dec, error_json, parse_int, decstr, d1, d0
from common import exceptions
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from gingernet.helper import check_api_token
from gingernet.models import (
    Banner, Link, Category, NavCat, ProductDocs,
    ProductAdvantage, ProductFunc, Costomer, Product,
    News, Solution, ContactUs, OnlineMsg, ApiAuth, Partner,
    CompanyIntro, TechTeam, DevHis, CompanyAdvantage, Research, CompanyValue
)
logger = logging.getLogger(__name__)


def global_variable(request):
    navcat_category_list = []
    nav_cat_list = NavCat.objects.all()
    link_list = Link.objects.all().order_by('-id')[:100]
    for nav_cat in nav_cat_list:
        category_list = Category.objects.filter(nav_cat=nav_cat)
        navcat_category = {
            "navcat": nav_cat,
            "category_lst": category_list,
        }
        navcat_category_list.append(navcat_category)
    return locals()


def index(request):
    chain_product_list = Product.objects.filter(product_cat='blockchain',is_del='NO')
    other_product_list = Product.objects.filter(product_cat='other', is_del='NO')
    company_adv_list = CompanyAdvantage.objects.filter(is_del='NO')
    solution_list = Solution.objects.filter(is_del='NO').order_by('-id')[0:3]
    news_list = News.objects.filter(is_del='NO').order_by('-id')[0:4]
    costomer_list = Costomer.objects.filter(is_del='NO').order_by('-id')
    return render(request, 'front/index.html', locals())


def product(request, id):
    category = Category.objects.get(id=id)
    product = Product.objects.get(category=category)
    return render(request, 'front/product.html', locals())


def solution(request, id):
    category = Category.objects.get(id=id)
    solution = Solution.objects.get(category=category)
    return render(request, 'front/solution.html', locals())


def research(request):
    research_lst = Research.objects.filter(is_del='No')
    return render(request, 'front/research.html', locals())


def comp_dyn(request):
    comp_dyn_list = News.objects.filter(is_del='No')
    comp_dyn_lists = paged_items(request, comp_dyn_list)
    return render(request, 'front/newsList.html', locals())


def partner(request):
    return render(request, 'front/partner.html', locals())


def about(request):
    return render(request, 'front/about.html', locals())
