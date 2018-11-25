# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from repository import models
import json
from datetime import datetime, date
# Create your views here.


class JsonEncode(json.JSONEncoder):
    """
    继承json，时间序列化
    """
    def default(self, value):
        if isinstance(value, datetime):
            return value.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(value, date):
            return value.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, value)


def curd(req):
    return HttpResponse('...')


def curd_json(request):
    table_config = [
        {'q': 'id', 'title': 'ID'},
        {'q': 'hostname', 'title': '主机'},
        {'q': 'create_at', 'title': '创建时间'},
        {'q': 'asset__cabinet_nu', 'title': '机柜号'},
        {'q':'asset__business_unit__name', 'title': '业务线名称'}]#用于查找数据库和前端显示中文,字典无序采用列表嵌套
    values_list = [i['q'] for i in table_config]
    server_list = models.Server.objects.values(*values_list)
    rel = {'table_config': table_config,
    'values_list': list(values_list)}#queryset转列表
    return HttpResponse(json.dumps(rel, cls=JsonEncode))