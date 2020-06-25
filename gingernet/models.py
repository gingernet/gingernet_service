#encoding=utf-8

from django.db import models
from common.model_fields import (DecField, IdField)
from common.models import BaseModel
from DjangoUeditor.models import UEditorField

DEL_CHOICES = [(x, x) for x in ['YES', 'NO']]


class ApiAuth(BaseModel):
    EXPIRE_CHOICES = [(x, x) for x in ['YES', 'NO']]
    STATUS_CHOICES = [(x, x) for x in ['UnVerify', 'Verifing', 'Verified']]
    name = models.CharField("接入名称", max_length=64, default='')
    api_token = models.CharField("接入 api Token", max_length=128, default='unknown')
    is_expire = models.CharField("Token是否过期", max_length=128, default="NO", choices=EXPIRE_CHOICES)
    status = models.CharField("API 审核状态", max_length=32, choices=STATUS_CHOICES, default='checking')

    class Meta:
        verbose_name = "API 授权表"
        verbose_name_plural = "API 授权表"

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            "name": self.name,
            "api_token": self.api_token,
            "is_expire": self.is_expire,
            "status":self.status,
        }


class Banner(BaseModel):
    text_info = models.CharField(max_length=50, default='', verbose_name=u'banner 信息')
    img = models.ImageField(upload_to='banner/', verbose_name=u'图片')
    link_url = models.URLField(max_length=100, default="", verbose_name=u'url链接')
    banner_mark = models.CharField(max_length=50, default='index', verbose_name=u'banner 标志')
    is_active = models.BooleanField(default=True, verbose_name=u'是否删除')

    def __str__(self):
        return self.text_info

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = "轮播图"


class Link(BaseModel):
    name = models.CharField(max_length=20, default="", verbose_name=u'名字')
    logo = models.ImageField(upload_to='logo_img/%Y/%m/%d/', blank=True, null=True, verbose_name=u'图片')
    linkurl = models.URLField(max_length=100, default="", verbose_name=u'URL链接')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "友情链接"
        verbose_name_plural = "友情链接"


class NavCat(BaseModel):
    name = models.CharField(max_length=20, default="", verbose_name=u'导航名称')
    nav_mark = models.CharField(max_length=20, default="", verbose_name=u'导航标志')

    class Meta:
        verbose_name = "导航列表"
        verbose_name_plural = "导航列表"

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'nav_mark': self.nav_mark
        }


class Category(BaseModel):
    name = models.CharField(max_length=20, default="", verbose_name=u'分类名称')
    nav_cat = models.ForeignKey(
        NavCat, related_name='nav_category', blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name=u'类别导航')
    index = models.IntegerField(default=999, verbose_name=u'索引')
    category_mark = models.CharField(max_length=20, default="", verbose_name=u'分类标志')

    class Meta:
        verbose_name = "分类列表"
        verbose_name_plural = "分类列表"

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'name': self.name,
            'index': self.index,
            'category_mark': self.category_mark
        }


class CompanyAdvantage(BaseModel):
    title = models.CharField(max_length=70, verbose_name=u'标题')
    excerpt = models.TextField(max_length=500, blank=True, default="", verbose_name=u'优势摘要')
    img = models.ImageField(upload_to='adv_img/%Y/%m/%d/', blank=True, null=True, verbose_name=u'优势图片')
    body = UEditorField(
        width=800, height=500, toolbars="full", imagePath="img/", filePath="upfile/",
        upload_settings={"imageMaxSize": 1204000}, settings={}, command=None, blank=True,
        verbose_name=u'优势详情'
    )
    is_del = models.CharField(max_length=16, choices=DEL_CHOICES, default='NO', verbose_name=u'是否删除')

    class Meta:
        verbose_name = "公司优势"
        verbose_name_plural = "公司优势"

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'img': str(self.img),
            'excerpt': self.excerpt,
            'body': self.body,
            'is_del': self.is_del
        }


class News(BaseModel):
    title = models.CharField(max_length=70, verbose_name=u'标题')
    excerpt = models.TextField(max_length=200, blank=True, default="", verbose_name=u'咨询摘要')
    category = models.ForeignKey(Category, related_name='news_category', blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name=u'类别')
    icon = models.ImageField(upload_to='news_icon/%Y/%m/%d/', blank=True, null=True, verbose_name=u'新闻封面')
    img = models.ImageField(upload_to='news_img/%Y/%m/%d/', blank=True, null=True, verbose_name=u'新闻封面')
    body = UEditorField(
        width=800, height=500, toolbars="full", imagePath="img/", filePath="upfile/",
        upload_settings={"imageMaxSize": 1204000}, settings={}, command=None, blank=True,
        verbose_name=u'新闻内容'
    )
    views = models.PositiveIntegerField(default=0, verbose_name=u'查看次数')
    author = models.CharField(max_length=70, default="知鱼定制", verbose_name=u'作者')
    is_del = models.CharField(max_length=16, choices=DEL_CHOICES, default='NO', verbose_name=u'是否删除')


    class Meta:
        verbose_name = "新闻管理"
        verbose_name_plural = "新闻管理"

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'excerpt': self.excerpt,
            'icon': str(self.icon),
            'img': str(self.img),
            'body': self.body,
            'views': self.views,
            'author': self.author,
            'is_del': self.is_del,
            'created_at':self.created_at
            }


class ProductFunc(BaseModel):
    name = models.CharField(max_length=70, default="", verbose_name=u'产品名称')
    excerpt = models.TextField(max_length=200, blank=True, default="", verbose_name=u'摘要')
    is_del = models.CharField(max_length=16, choices=DEL_CHOICES, default='NO', verbose_name=u'是否删除')

    class Meta:
        verbose_name = "产品功能表"
        verbose_name_plural = "产品功能表"

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'excerpt': self.excerpt,
            'is_del': self.is_del,
            'created_at': self.created_at
        }


class ProductAdvantage(BaseModel):
    name = models.CharField(max_length=70, default="", verbose_name=u'名称')
    excerpt = models.TextField(max_length=200, blank=True, default="", verbose_name=u'摘要')
    is_del = models.CharField(max_length=16, choices=DEL_CHOICES, default='NO', verbose_name=u'是否删除')

    class Meta:
        verbose_name = "产品优势表"
        verbose_name_plural = "产品优势表"

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'excerpt': self.excerpt,
            'is_del': self.is_del,
            'created_at': self.created_at
        }


class ProductDocs(BaseModel):
    name = models.CharField(max_length=70, default="", verbose_name=u'名称')
    img = models.ImageField(upload_to='docs_img/%Y/%m/%d/', blank=True, null=True, verbose_name=u'图片')
    excerpt = models.TextField(max_length=200, blank=True, default="", verbose_name=u'摘要')
    detail = UEditorField(
        width=800, height=500, toolbars="full", imagePath="img/", filePath="upfile/",
        upload_settings={"imageMaxSize": 1204000}, settings={}, command=None, blank=True,
        verbose_name=u'详情'
    )
    is_del = models.CharField(max_length=16, choices=DEL_CHOICES, default='NO', verbose_name=u'是否删除')

    class Meta:
        verbose_name = "产品接口文档"
        verbose_name_plural = "产品接口文档"

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'img': str(self.img),
            'excerpt': self.excerpt,
            'detail': self.detail,
            'is_del': self.is_del,
            'created_at': self.created_at
        }


class Partnet(BaseModel):
    name = models.CharField(max_length=70, default="", verbose_name=u'名称')
    logo = models.ImageField(upload_to='cos_logo/%Y/%m/%d/', blank=True, null=True, verbose_name=u'Logo')
    excerpt = models.TextField(max_length=200, blank=True, default="", verbose_name=u'摘要')
    is_del = models.CharField(max_length=16, choices=DEL_CHOICES, default='NO', verbose_name=u'是否删除')

    class Meta:
        verbose_name = "合作伙伴表"
        verbose_name_plural = "合作伙伴表"

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'logo': str(self.logo),
            'excerpt': self.excerpt,
            'is_del': self.is_del,
            'created_at': self.created_at
        }


class Costomer(BaseModel):
    name = models.CharField(max_length=70, default="", verbose_name=u'名称')
    logo = models.ImageField(upload_to='cos_logo/%Y/%m/%d/', blank=True, null=True, verbose_name=u'Logo')
    excerpt = models.TextField(max_length=200, blank=True, default="", verbose_name=u'摘要')
    is_del = models.CharField(max_length=16, choices=DEL_CHOICES, default='NO', verbose_name=u'是否删除')

    class Meta:
        verbose_name = "产品客户表"
        verbose_name_plural = "产品客户表"

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'logo': str(self.logo),
            'excerpt': self.excerpt,
            'is_del': self.is_del,
            'created_at': self.created_at
        }


class Product(BaseModel):
    PCAT_CHOICES = [(x, x) for x in ['blockchain', 'other']]
    name = models.CharField(max_length=70, default="", verbose_name=u'产品名称')
    excerpt = models.TextField(max_length=200, blank=True, default="", verbose_name=u'摘要')
    icon = models.ImageField(upload_to='product_icon/%Y/%m/%d/', blank=True, null=True, verbose_name=u'图片')
    img = models.ImageField(upload_to='product_img/%Y/%m/%d/', blank=True, null=True, verbose_name=u'图片')
    category = models.ForeignKey(Category, related_name='product_category', blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name=u'分类')
    views = models.PositiveIntegerField(default=0)
    detail = UEditorField(
        width=800, height=500, toolbars="full", imagePath="img/", filePath="upfile/",
        upload_settings={"imageMaxSize": 1204000}, settings={}, command=None, blank=True,
        verbose_name=u'详情'
    )
    product_func = models.ManyToManyField(ProductFunc, blank=True, null=True, verbose_name=u'产品功能')
    product_adv = models.ManyToManyField(ProductAdvantage, blank=True, null=True, verbose_name=u'产品优势')
    product_doc = models.ManyToManyField(ProductDocs, blank=True, null=True, verbose_name=u'产品文档')
    product_cos = models.ManyToManyField(Costomer, blank=True, null=True, verbose_name=u'客户案例')
    product_cat = models.CharField(max_length=70, choices=PCAT_CHOICES, default="blockchain", verbose_name=u'产品名称')
    is_del = models.CharField(max_length=16, choices=DEL_CHOICES, default='NO', verbose_name=u'是否删除')

    class Meta:
        verbose_name = "产品列表"
        verbose_name_plural = "产品列表"

    def __str__(self):
        return self.name

    def get_product_func(self):
        func_list = self.product_func.values('id', 'name', 'excerpt').all()
        return list(func_list)

    def get_product_adv(self):
        adv_list = self.product_adv.values('id', 'name', 'excerpt').all()
        return list(adv_list)

    def get_product_docs(self):
        docs_list = self.product_doc.values('id', 'name', 'img', 'excerpt', 'detail').all()
        return list(docs_list)

    def get_product_cos(self):
        cos_list = self.product_cos.values('id', 'name', 'logo', 'excerpt').all()
        return list(cos_list)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'excerpt': self.excerpt,
            'icon': str(self.icon),
            'img': str(self.img),
            'views': self.views,
            'product_func': self.get_product_func(),
            'product_adv': self.get_product_adv(),
            'product_docs': self.get_product_docs(),
            'product_cos': self.get_product_cos(),
            'product_cat': self.product_cat,
            'detail': self.detail,
            'is_del': self.is_del,
            'created_at':self.created_at
        }


class Solution(BaseModel):
    name = models.CharField(max_length=70, default="", verbose_name=u'方案名称')
    excerpt = models.TextField(max_length=200, blank=True, default="", verbose_name=u'方案摘要')
    img = models.ImageField(upload_to='solution_img/%Y/%m/%d/', blank=True, null=True, verbose_name=u'方案图片')
    category = models.ForeignKey(
        Category, related_name='solution_category', blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name=u'方案分类'
    )
    views = models.PositiveIntegerField(default=0, verbose_name=u'方案查看次数')
    detail = UEditorField(
        width=800, height=500, toolbars="full", imagePath="img/", filePath="upfile/",
        upload_settings={"imageMaxSize": 1204000}, settings={}, command=None, blank=True,
        verbose_name=u'方案详情'
    )
    is_del = models.CharField(max_length=16, choices=DEL_CHOICES, default='NO', verbose_name=u'是否删除')

    class Meta:
        verbose_name = "解决方案表"
        verbose_name_plural = "解决方案表"

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'excerpt': self.excerpt,
            'img': str(self.img),
            'views': self.views,
            'detail': self.detail,
            'is_del': self.is_del,
            'created_at':self.created_at
        }


class Research(BaseModel):
    name = models.CharField(max_length=70, default="", verbose_name=u'研究标题')
    excerpt = models.TextField(max_length=200, blank=True, default="", verbose_name=u'研究摘要')
    img = models.ImageField(upload_to='solution_img/%Y/%m/%d/', blank=True, null=True, verbose_name=u'研究图片')
    category = models.ForeignKey(
        Category, related_name='research_category', blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name=u'研究分类'
    )
    pdf_file = models.FileField("pdf文件", upload_to='pdf_file/%Y/%m/%d/', blank=True, null=True)
    views = models.PositiveIntegerField(default=0, verbose_name=u'研究内容查看次数')
    author = models.CharField(max_length=70, default="知鱼定制", verbose_name=u'作者')
    detail = UEditorField(
        width=800, height=500, toolbars="full", imagePath="img/", filePath="upfile/",
        upload_settings={"imageMaxSize": 1204000}, settings={}, command=None, blank=True,
        verbose_name=u'研究内容'
    )
    is_del = models.CharField(max_length=16, choices=DEL_CHOICES, default='NO', verbose_name=u'是否删除')

    class Meta:
        verbose_name = "研究中心表"
        verbose_name_plural = "研究中心表"

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'excerpt': self.excerpt,
            'img': str(self.img),
            'views': self.views,
            'pdf_file': str(self.pdf_file),
            'detail': self.detail,
            'author': self.author,
            'is_del': self.is_del,
            'created_at':self.created_at
        }


class Case(BaseModel):
    title = models.CharField(max_length=70, default="", verbose_name=u'案例标题')
    img = models.ImageField(upload_to='case_img/%Y/%m/%d/', blank=True, null=True, verbose_name=u'案例图片')
    body = UEditorField(
        width=800, height=500, toolbars="full", imagePath="img/", filePath="upfile/",
        upload_settings={"imageMaxSize": 1204000}, settings={}, command=None, blank=True,
        verbose_name=u'案例内容'
    )
    nav_cat = models.ForeignKey(NavCat, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name=u'案例分类')
    views = models.PositiveIntegerField(default=0, verbose_name=u'案例查看次数')
    is_del = models.CharField(max_length=16, choices=DEL_CHOICES, default='NO', verbose_name=u'是否删除')

    class Meta:
        verbose_name = "客户案例"
        verbose_name_plural = "客户案例"

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'id': self.id,
            'img': str(self.img),
            'body': self.body,
            'nav_cat': self.nav_cat,
            'views': self.views,
            'is_del': self.is_del,
            'created_at': self.created_at
        }


class ContactUs(BaseModel):
    qq = models.CharField(max_length=70, default='1294928442', verbose_name=u'QQ')
    phone = models.CharField(max_length=70, default='13611267041',  verbose_name=u'电话')
    email = models.CharField(max_length=70, default='guoshijiang2012@163.com', verbose_name=u'邮箱')
    img = models.ImageField(upload_to='weima_img/%Y/%m/%d/', blank=True, null=True, verbose_name=u'微信二维码')
    is_del = models.CharField(max_length=16, choices=DEL_CHOICES, default='NO', verbose_name=u'是否删除')

    class Meta:
        verbose_name = "联系我们"
        verbose_name_plural = "联系我们"

    def __str__(self):
        return self.qq

    def to_dict(self):
        return {
            'id': self.id,
            'qq': self.qq,
            'phone': self.phone,
            'email': self.email,
            'img': str(self.img),
            'created_at': self.created_at
        }


class OnlineMsg(BaseModel):
    HANDLE_CHOICES = [(x, x) for x in ['YES', 'NO']]
    name = models.CharField(max_length=70, verbose_name=u'姓名')
    phone = models.CharField(max_length=70, verbose_name=u'电话')
    email = models.CharField(max_length=70, verbose_name=u'邮箱')
    weichat = models.CharField(max_length=70, verbose_name=u'邮箱')
    content = models.TextField(max_length=500, blank=True, default="", verbose_name=u'留言内容')
    is_handle = models.CharField(max_length=16, choices=HANDLE_CHOICES, default='NO', verbose_name=u'是否处理')
    is_del = models.CharField(max_length=16, choices=DEL_CHOICES, default='NO', verbose_name=u'是否删除')

    class Meta:
        verbose_name = "在线咨询"
        verbose_name_plural = "在线咨询"

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'weichat': self.weichat,
            'content': self.content,
            'is_handle': self.is_handle,
            'is_del': self.is_del,
            'created_at': self.created_at
        }


class CompanyIntro(BaseModel):
    name = models.CharField(max_length=70, verbose_name=u'公司名字')
    detail = UEditorField(
        width=800, height=500, toolbars="full", imagePath="img/", filePath="upfile/",
        upload_settings={"imageMaxSize": 1204000}, settings={}, command=None, blank=True,
        verbose_name=u'公司详情'
    )
    is_del = models.CharField(max_length=16, choices=DEL_CHOICES, default='NO', verbose_name=u'是否删除')

    class Meta:
        verbose_name = "公司介绍"
        verbose_name_plural = "公司介绍"

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'detail': self.detail,
            'is_del': self.is_del,
            'created_at': self.created_at
        }


class TechTeam(BaseModel):
    name = models.CharField(max_length=70, verbose_name=u'团队名字')
    detail = UEditorField(
        width=800, height=500, toolbars="full", imagePath="img/", filePath="upfile/",
        upload_settings={"imageMaxSize": 1204000}, settings={}, command=None, blank=True,
        verbose_name=u'团队详情'
    )
    is_del = models.CharField(max_length=16, choices=DEL_CHOICES, default='NO', verbose_name=u'是否删除')

    class Meta:
        verbose_name = "技术团队"
        verbose_name_plural = "技术团队"

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'detail': self.detail,
            'is_del': self.is_del,
            'created_at': self.created_at
        }


class DevHis(BaseModel):
    period = models.CharField(max_length=70, verbose_name=u'时间段')
    detail = models.TextField(max_length=200, blank=True, default="", verbose_name=u'发展概述')
    is_del = models.CharField(max_length=16, choices=DEL_CHOICES, default='NO', verbose_name=u'是否删除')

    class Meta:
        verbose_name = "发展历程"
        verbose_name_plural = "发展历程"

    def __str__(self):
        return self.period

    def to_dict(self):
        return {
            'id': self.id,
            'period': self.period,
            'detail': self.detail,
            'is_del': self.is_del,
            'created_at': self.created_at
        }

