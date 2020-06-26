from django.conf.urls import url
from api.v1.api import (
    get_index, get_nav_cat, get_product_list, get_product_detail_by_id,
    get_product_detail_by_cat, get_product_docs, get_news_list, get_news_detail,
    get_solution_list, get_solution_detail, get_partner_list, create_online_msg, get_about,
    get_resarch_list, get_research_detail, get_partner_detail
)

urlpatterns = [
    # 导航和首页接口
    url('get_nav_cat/', get_nav_cat),
    url('get_index/', get_index),

    # 产品
    url('get_product_list/', get_product_list),
    url('get_product_detail_by_cat', get_product_detail_by_cat),
    url('get_product_detail_by_id/', get_product_detail_by_id),
    url('get_product_docs/', get_product_docs),

    # 新闻接口
    url('get_news_list/', get_news_list),
    url('get_news_detail/', get_news_detail),

    # 解决方案接口
    url('get_solution_list/', get_solution_list),
    url('get_solution_detail/', get_solution_detail),

    # 研究中心相关接口
    url('get_resarch_list/', get_resarch_list),
    url('get_research_detail/', get_research_detail),

    # 获取客户列表
    url('get_partner_list/', get_partner_list),
    url('get_partner_detail', get_partner_detail),

    # 创建在线消息
    url('create_online_msg/', create_online_msg),

    # 关于我们
    url('get_about/', get_about),
]