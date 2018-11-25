# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
table_config = [
    {'q': 'id', 'title': 'ID'},
    {'q': 'hostname', 'title': '主机'},
    {'q': 'create_at', 'title': '创建时间'},
    {'q': 'asset__cabinet_nu', 'title': '机柜号'},
    {'q': 'asset__business_unit__name', 'title': '业务线名称'}]  # 用于查找数据库和前端显示中文,字典无序采用列表嵌套
values_list = [i['q'] for i in table_config]
print(values_list)