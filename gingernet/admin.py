from django.contrib import admin
from gingernet.models import (
    Banner, Link, Category, NavCat, ProductDocs,
    ProductAdvantage, ProductFunc, Costomer, Product,
    News, Solution, ContactUs, OnlineMsg, ApiAuth, Partner,
    CompanyIntro, TechTeam, DevHis, Research, CompanyAdvantage,
    CompanyValue, SolutionAdvantage, SolutionWindControl
)

@admin.register(Partner)
class PartnerValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'excerpt', 'is_del')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'name')


@admin.register(CompanyValue)
class CompanyValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'excerpt', 'is_del')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'name')


@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'excerpt', 'is_del')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'name')


@admin.register(CompanyAdvantage)
class CompanyAdvantageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'excerpt', 'is_del')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'title')


@admin.register(ApiAuth)
class ApiAuthAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'api_token', 'is_expire', 'status')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'name')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'img')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'img')


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'name')


@admin.register(NavCat)
class NavCatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'name')


@admin.register(ProductAdvantage)
class ProductAdvantageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_per_page = 50
    ordering = ('-created_at',)


@admin.register(ProductFunc)
class ProductFuncAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_per_page = 50
    ordering = ('-created_at',)


@admin.register(ProductDocs)
class ProductDocsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_per_page = 50
    ordering = ('-created_at',)


@admin.register(Costomer)
class CostomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_per_page = 50
    ordering = ('-created_at',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'views', 'created_at')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'title')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'name')


@admin.register(ContactUs)
class ContactUsPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'qq', 'phone', 'email', 'created_at')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'phone')


@admin.register(SolutionAdvantage)
class SolutionAdvantageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'excerpt', 'created_at')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'title')


@admin.register(SolutionWindControl)
class SolutionWindControlAdvantageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'excerpt', 'created_at')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'title')


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'views', 'created_at')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'name')


@admin.register(OnlineMsg)
class OnlineMsgPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'content', 'is_handle', 'is_del', 'created_at')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'name')


@admin.register(CompanyIntro)
class CompanyIntroAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'name')


@admin.register(TechTeam)
class TechTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'name')


@admin.register(DevHis)
class DevHisAdmin(admin.ModelAdmin):
    list_display = ('id', 'period', 'created_at')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'period')


