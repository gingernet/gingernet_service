#encoding=utf-8

import logging
from gingernet.models import ApiAuth
from common.helpers import error_json

TOEKN_INFO_EMPTY = 1001
API_TOKEN_NOT_EXIST = 1002
API_TOKEN_STATUS = 1003
API_TOKEN_EXPIRE = 1004

def check_api_token(func):
    def api_auth(request, *args, ** kwargs):
        api_token = request.META.get("HTTP_API_TOKEN")
        logging.info("api_token=%s ", api_token)
        if api_token in ["", "None", None, "unkown"]:
            return error_json("Api Token 为空", TOEKN_INFO_EMPTY)
        api_auth = ApiAuth.objects.filter(api_token=api_token).first()
        if api_auth is None:
            return error_json("Api Token 不存在", API_TOKEN_NOT_EXIST)
        if api_auth.status in ['UnVerify', 'Verifing']:
            return error_json("Api Token 审核中", API_TOKEN_STATUS)
        if api_auth.is_expire == "YES":
            return API_TOKEN_EXPIRE
        return func(request, *args, **kwargs)
    return api_auth