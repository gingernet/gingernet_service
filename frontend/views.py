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
    cp_list = Product.objects.filter(product_cat='blockchain',is_del='NO').all()
    sl_list = Solution.objects.filter(is_del='NO').all()
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
    partner_list = Partner.objects.filter(is_del='NO').order_by('-id')
    fronted_nav_mark = 'index'
    return render(request, 'front/index.html', locals())


def product(request, id):
    category = Category.objects.get(id=id)
    product = Product.objects.get(category=category)
    fronted_nav_mark = 'product'
    return render(request, 'front/product.html', locals())


def solution(request, id):
    category = Category.objects.get(id=id)
    solution = Solution.objects.get(category=category)
    fronted_nav_mark = 'solution'
    return render(request, 'front/solution.html', locals())


def research(request):
    research_lst = Research.objects.filter(is_del='No')
    fronted_nav_mark = 'research'
    return render(request, 'front/research.html', locals())


def comp_dyn(request):
    comp_dyn_list = News.objects.filter(is_del='No')
    comp_dyn_lists = paged_items(request, comp_dyn_list)
    fronted_nav_mark = 'comp_dyn'
    return render(request, 'front/news_list.html', locals())


def comp_dyn_detail(request, id):
    dyn_detail = News.objects.get(id=id)
    comp_dyn_list = News.objects.filter(is_del='No')[:10]
    fronted_nav_mark = 'comp_dyn'
    return render(request, 'front/news_detail.html', locals())


def partner(request):
    fronted_nav_mark = 'partner'
    return render(request, 'front/partner.html', locals())


def about(request):
    fronted_nav_mark = 'about'
    return render(request, 'front/about.html', locals())


def online_msg(request):
    user_name = request.GET.get('user_name', "")
    phone = request.GET.get('phone', "")
    weichat = request.GET.get('weichat', "")
    email = request.GET.get('email', "")
    describe = request.GET.get('describe', "")
    OnlineMsg.objects.create(
        name=user_name,
        phone=phone,
        email=email,
        weichat=weichat,
        content=describe,
        is_handle="No",
        is_del="No",
    )
    return ok_json(None)
