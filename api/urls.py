from django.conf.urls import url
from api.v1.api import (
    get_index, get_banners, get_links, get_nav_cat,
    get_product_list, get_product_detail, get_product_docs,
    get_news_list, get_news_detail, get_solution_list,
    get_solution_detail, get_cos_list, create_online_msg, get_about
)

urlpatterns = [
    # 公共接口
    url('get_banners/', get_banners),
    url('get_links/', get_links),
    url('get_nav_cat/', get_nav_cat),

    # 首页
    url('get_index/', get_index),

    # 产品
    url('get_product_list/', get_product_list),
    url('get_product_detail/', get_product_detail),
    url('get_product_docs/', get_product_docs),

    # 新闻接口
    url('get_news_list/', get_news_list),
    url('get_news_detail/', get_news_detail),

    # 解决方案接口
    url('get_solution_list/', get_solution_list),
    url('get_solution_detail/', get_solution_detail),

    # 获取客户列表
    url('get_cos_list/', get_cos_list),

    # 创建在线消息
    url('create_online_msg/', create_online_msg),

    # 关于我们
    url('get_about/', get_about),
]