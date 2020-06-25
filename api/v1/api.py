#encoding=utf-8

import uuid
import time
import logging
from typing import Dict, Any
from functools import wraps
from decimal import Decimal
from django.http import HttpResponse, HttpRequest, JsonResponse, Http404
from django.conf import settings
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from common.helpers import ok_json, dec, error_json, parse_int, decstr, d1, d0
from common import exceptions
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from gingernet.helper import check_api_token
from gingernet.models import (
    Banner, Link, Category, NavCat, ProductDocs,
    ProductAdvantage, ProductFunc, Costomer, Product,
    News, Solution, ContactUs, OnlineMsg, ApiAuth,
    CompanyIntro, TechTeam, DevHis, CompanyAdvantage, Research)


logger = logging.getLogger(__name__)


def catch_error(func):
    def __wrap(request, *args, **kwargs):
        try:
            return func(request, *args, **kwargs)
        except exceptions.BaseException as e:
            logger.warning('api error %s', e.message)
            return error_json(e.message, code=e.code)
        except Http404:
            logger.warning('api error 404')
            return error_json('not found', code=404)
        except:
            logger.error('bad api request', exc_info=True)
            raise
    return __wrap


# 获取 banner 图接口
@csrf_exempt
@catch_error
@check_api_token
def get_banners(request):
    banner_mark = request.POST.get('banner_mark', "")
    banner_list = Banner.objects.values(
        "id", "text_info", "img", "banner_mark", "link_url").all()
    if banner_mark not in ["", None]:
        banner_list = banner_list.filter(banner_mark=banner_mark)
    banner_list = banner_list.order_by('-id')
    banner_list = banner_list[0:6]
    return ok_json((list(banner_list)))


# 获取友情链接接口
@csrf_exempt
@catch_error
@check_api_token
def get_links(request):
    link_list = Link.objects.values(
        "name", "logo", "linkurl").all()
    return ok_json(list(link_list))


# 获取导航条和分类
@csrf_exempt
@catch_error
@check_api_token
def get_nav_cat(request):
    navcat_category_list = []
    category_list = Category.objects.all()
    nav_cat_list = NavCat.objects.all()
    for nav_cat in nav_cat_list:
        category_lists = []
        for category in category_list:
            if nav_cat.id == category.nav_cat.id:
                category_item = {
                    "id":  category.id,
                    "name": category.name,
                    "category_mark": category.category_mark,
                }
                category_lists.append(category_item)
        navcat_item = {
            'id': nav_cat.id,
            'name': nav_cat.name,
            'nav_mark': nav_cat.nav_mark,
            'category': category_lists,
        }
        navcat_category = {
            'navcat': navcat_item,
        }
        navcat_category_list.append(navcat_category)
    return ok_json(list(navcat_category_list))


# 首页接口
@csrf_exempt
@catch_error
@check_api_token
def get_index(request):
    banner_list = Banner.objects.values(
        'id', 'text_info', 'img', 'link_url').filter(banner_mark='index', is_active=True)[0:6]
    chain_product_list = Product.objects.values(
        'id', 'name', 'icon', 'img', 'excerpt').filter(product_cat='blockchain',is_del='NO')
    other_product_list = Product.objects.values(
        'id', 'name', 'icon', 'img', 'excerpt').filter(product_cat='other', is_del='NO')
    company_adv_list = CompanyAdvantage.objects.values(
        'id', 'title', 'excerpt').filter(is_del='NO')
    solution_list = Solution.objects.values(
        'id', 'name', 'img', 'excerpt').filter(is_del='NO').order_by('-id')[0:3]
    news_list = News.objects.values(
        'id', 'title', 'icon', 'img', 'created_at').filter(is_del='NO').order_by('-id')[0:6]
    costomer_list = Costomer.objects.values(
        'id', 'name', 'logo', 'excerpt').filter(is_del='NO').order_by('-id')
    index_data = {
        "banner": list(banner_list),
        "chain_product": list(chain_product_list),
        "company_adv": list(company_adv_list),
        "other_product": list(other_product_list),
        "solution": list(solution_list),
        "costomer": list(costomer_list),
        "news": list(news_list),
    }
    return ok_json(index_data)


# 产品列表接口
@csrf_exempt
@catch_error
@check_api_token
def get_product_list(request):
    page = request.POST.get('page', 0)
    number = request.POST.get('number', 20)
    cat_id = request.POST.get('cat_id', 0)
    product_lists = Product.objects.values(
        "id", "name", 'excerpt', "category", "icon", "img", 'detail').all()

    if cat_id not in ['0', 0, ""]:
        category = Category.objects.get(id=cat_id)
        product_lists = product_lists.filter(category = category)

    paginator = Paginator(product_lists, number)
    try:
        product_lists = paginator.page(page)
    except PageNotAnInteger:
        product_lists = paginator.page(1)
    except EmptyPage:
        product_lists = paginator.page(paginator.num_pages)
    return ok_json(list(product_lists))


# 产品详情接口
@csrf_exempt
@catch_error
@check_api_token
def get_product_detail(request):
    pro_id = request.POST.get('pro_id', 0)
    product = Product.objects.get(id=pro_id)
    return ok_json(product.to_dict())


# 阅读产品接口文档
@csrf_exempt
@catch_error
@check_api_token
def get_product_docs(request):
    doc_id = request.POST.get('doc_id', 0)
    product_doc = ProductDocs.objects.get(id=doc_id)
    return ok_json(product_doc.to_dict())


# 新闻列表列表
@csrf_exempt
@catch_error
@check_api_token
def get_news_list(request):
    page = request.POST.get('page', 0)
    number = request.POST.get('number', 20)
    cat_id = request.POST.get('cat_id', 0)

    news_lists = News.objects.values(
        "id", "title", 'excerpt', "category",
        "img", "icon", 'views', 'author', 'created_at').all()

    if cat_id not in ['0', 0, ""]:
        category = Category.objects.get(id=cat_id)
        news_lists = news_lists.filter(category=category)

    paginator = Paginator(news_lists, number)
    try:
        news_lists = paginator.page(page)
    except PageNotAnInteger:
        news_lists = paginator.page(1)
    except EmptyPage:
        news_lists = paginator.page(paginator.num_pages)
    return ok_json(list(news_lists))


# 新闻详情页
@csrf_exempt
@catch_error
@check_api_token
def get_news_detail(request):
    n_id = request.POST.get('n_id', 0)
    news = News.objects.get(id=n_id)
    news.views += 1
    news.save()
    return ok_json(news.to_dict())


# 研究中心列表
@csrf_exempt
@catch_error
@check_api_token
def get_resarch_list(request):
    page = request.POST.get('page', 0)
    number = request.POST.get('number', 20)
    cat_id = request.POST.get('cat_id', 0)
    research_list = Research.objects.values(
        "id", "name", 'excerpt', "category",
        "img", "pdf_file", 'views', 'author', 'created_at').all()
    if cat_id not in ['0', 0, ""]:
        category = Category.objects.get(id=cat_id)
        research_list = research_list.filter(category=category)
    paginator = Paginator(research_list, number)
    try:
        research_list = paginator.page(page)
    except PageNotAnInteger:
        research_list = paginator.page(1)
    except EmptyPage:
        research_list = paginator.page(paginator.num_pages)
    return ok_json(list(research_list))


# 新闻详情页
@csrf_exempt
@catch_error
@check_api_token
def get_research_detail(request):
    r_id = request.POST.get('r_id', 0)
    researchs = Research.objects.get(id=r_id)
    researchs.views += 1
    researchs.save()
    return ok_json(researchs.to_dict())


# 解决方案列表
@csrf_exempt
@catch_error
@check_api_token
def get_solution_list(request):
    page = request.POST.get('page', 0)
    number = request.POST.get('number', 20)
    cat_id = request.POST.get('cat_id', 0)

    solution_lists = Solution.objects.values(
        "id", "name", 'excerpt', "category",
        "img", 'created_at').all()

    if cat_id not in ['0', 0, ""]:
        category = Category.objects.get(id=cat_id)
        solution_lists = solution_lists.filter(category=category)

    paginator = Paginator(solution_lists, number)
    try:
        solution_lists = paginator.page(page)
    except PageNotAnInteger:
        solution_lists = paginator.page(1)
    except EmptyPage:
        solution_lists = paginator.page(paginator.num_pages)
    return ok_json(list(solution_lists))


# 解决方案详情
@csrf_exempt
@catch_error
@check_api_token
def get_solution_detail(request):
    sol_id = request.POST.get('sol_id', 0)
    solution = Solution.objects.get(id=sol_id)
    return ok_json(solution.to_dict())


# 解决方案详情
@csrf_exempt
@catch_error
@check_api_token
def get_cos_list(request):
    cos_list = Costomer.objects.values(
        'id', 'name', 'logo', 'excerpt').all()
    return ok_json(list(cos_list))


# 解决方案详情
@csrf_exempt
@catch_error
@check_api_token
def create_online_msg(request):
    name = request.POST.get('name', "")
    phone = request.POST.get('phone', "")
    email = request.POST.get('email', "")
    weichat = request.POST.get('weichat', "")
    content = request.POST.get('content', "")
    logging.info("name = %s and phone = %s and email = %s and content = %s weichat = %s",
                 name, phone, email, content, weichat)
    if name in ["", None]:
        return error_json("用户名不能为空", 1000)
    if phone in ["", None]:
        return error_json("手机号不能为空", 1000)
    if email in ["", None]:
        return error_json("电子邮件不能为空", 1000)
    if weichat in ["", None]:
        return error_json("微信不能为空", 1000)
    if content in ["", None]:
        return error_json("内容不能为空", 1000)
    on_msg = OnlineMsg.objects.create(
        name=name,
        phone=phone,
        email=email,
        weichat=weichat,
        content=content,
    )
    return ok_json(on_msg.to_dict())


@csrf_exempt
@catch_error
@check_api_token
def get_about(request):
    company_intro = CompanyIntro.objects.filter(is_del='NO').first()
    tech_team = TechTeam.objects.filter(is_del='NO').first()
    dev_his_list = DevHis.objects.values(
        'period', 'detail').filter(is_del='NO').order_by('-id')
    contract_us = ContactUs.objects.filter(is_del='NO').first()
    ret_data = {
        'company_intro': company_intro.to_dict(),
        'tech_team': tech_team.to_dict(),
        'dev_his_list': list(dev_his_list),
        'contract_us': contract_us.to_dict(),
    }
    return ok_json(ret_data)
