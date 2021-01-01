#encoding=utf-8

from urllib.parse import urljoin
import pytz
import json
import time

from django.conf import settings
from django import template
from django.contrib.contenttypes.models import ContentType
from decimal import Decimal


register = template.Library()


@register.filter(name='hdatetime')
def repr_datetime(value) -> str:
    if not value:
        return ''
    tz = pytz.timezone(settings.TIME_ZONE)
    #return value.astimezone(tz), "%Y-%m-%d %H:%M")
    #return str(value.astimezone(tz))
    #return value.astimezone(tz).replace(microsecond=0).isoformat()
    return value.astimezone(tz).strftime('%Y-%m-%d %H:%M:%S')

@register.filter(name='hdate')
def repr_date(value):
    if not value:
        return ''
    tz = pytz.timezone(settings.TIME_ZONE)
    return value.astimezone(tz).strftime("%Y-%m-%d")

@register.filter(name='hdatemin')
def repr_datemin(value):
    if not value:
        return ''
    else:
        loc_time = time.localtime(int(value))
        return time.strftime("%Y-%m-%d %H:%M", loc_time)

@register.filter(name='keep_two_decimal_places')
def ktd_places(value):
    if not value:
        return "0"
    dec_value = Decimal(value).quantize(Decimal("0.00000000"))
    return dec_value.to_integral() if dec_value == dec_value.to_integral() else dec_value.normalize()

@register.filter(name='decimal_remove_zero')
def remove_zero(value):
    if not value:
        return "0"
    return value.to_integral() if value == value.to_integral() else value.normalize()

@register.filter(name='empty_qty_abs')
def empty_qty(value):
    if not value:
        return "0"
    return abs(value).to_integral() if value == value.to_integral() else value.normalize()


@register.filter(name='array_length')
def array_length(value)->int:
    print(value)
    return len(value)
