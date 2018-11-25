# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from repository import models
from django.shortcuts import HttpResponse, render
from django.conf import settings
import time
import json
# Create your views here.
api_key_record = {
    # "1b96b89695f52ec9de8292a5a7945e38|1501472467.4977243":1501472477.4977243
}


def decrypt(msg):
    from Crypto.Cipher import AES
    key = b'dfdsdfsasdfdsdfs'
    cipher = AES.new(key, AES.MODE_CBC, key)
    result = cipher.decrypt(msg)
    data = result[0:-result[-1]]
    return str(data, encoding='utf-8')


def asset(request):
    import hashlib
    client_md5_time_key = request.META.get('HTTP_OPENKEY')
    client_md5_key, client_ctime =  client_md5_time_key.split('|')
    client_ctime = float(client_ctime)
    server_time = time.time()

    if server_time-client_ctime > 10:
        return HttpResponse('超时')
    temp = '%s|%s' %(settings.AUTH_KEY, client_ctime)
    m = hashlib.md5()
    m.update(bytes(temp, encoding='utf-8'))
    server_md5_key = m.hexdigest()
    if server_md5_key != client_md5_key:
        return HttpResponse('时间错误了')

    for k in list(api_key_record.keys()):
        if server_time > api_key_record[k]:
            del api_key_record[k]

    if client_md5_time_key in api_key_record:
        return HttpResponse('有人来过了')
    else:
        api_key_record[client_md5_time_key] = client_ctime + 10
        if server_md5_key != client_md5_key:
            return HttpResponse('认证不通过')
    if request.method == 'GET':
        return HttpResponse('不适用查看')
    elif request.method == 'POST':
        server_info = decrypt(request.body)
        server_info = json.loads(server_info)
        hostname = server_info['basic']['data']['hostname']
        server_obj = models.Server.objects.filter(hostname=hostname).first()#原来的数据
        if not server_obj:
            return HttpResponse('当前主机不存在')
        for k, v in server_obj.items():
            print(k, v)
        if not server_info['disk']['status']:
            models.ErrorLog.objects.create(content=server_info['disk']['data'], asset_obj=server_obj.asset, title='【%s】硬盘采集错误信息' % hostname)
        new_disk_dict = server_info['disk']['data']
        old_disk_list = models.Disk.objects.fileter(server_obj=server_obj)
        new_slot_list = list(new_disk_dict.keys())
        old_slot_list = []
        for item in old_disk_list:
            old_slot_list.append(item.slot)
        # 交集：更新[5,]
        update_list = set(new_slot_list).intersection(old_slot_list)
        # 差集: 创建[3]
        create_list = set(new_slot_list).difference(old_slot_list)
        # 差集: 创建[4]
        del_list = set(old_slot_list).difference(new_slot_list)
        if del_list:#删除
            models.Disk.objects.filter(server_obj=server_obj, slot__in=del_list).delete()
            models.AssetRecord.objects.create(asset_obj=server_obj.asset, content="移除硬盘：%s" % ("、".join(del_list),))
        record_list = []
        for slot in create_list:
            disk_dict = new_disk_dict[slot]
            disk_dict['server_obj'] = server_obj
            models.Disk.objects.create(**disk_dict)
            temp = "新增硬盘:位置{slot},容量{capacity},型号:{model},类型:{pd_type}".format(**disk_dict)
            record_list.append(temp)
        if record_list:
            content = ";".join(record_list)
            models.AssetRecord.objects.create(asset_obj=server_obj.asset, content=content)

        # ############ 更新 ############
        record_list = []
        row_map = {'capacity': '容量','pd_type': '类型','model':'型号'}
        for slot in update_list:
            new_dist_row = new_disk_dict[slot]
            ol_disk_row = models.Disk.objects.filter(slot=slot, server_obj=server_obj).first()
            for k, v in new_dist_row.items():
                # k: capacity;slot;pd_type;model
                # v: '476.939''xxies              DXM05B0Q''SATA'
                value = getattr(ol_disk_row,k)
                if v != value:
                    record_list.append("槽位%s,%s由%s变更为%s" %(slot, row_map[k], value, v,))
                    setattr(ol_disk_row, k, v)
            ol_disk_row.save()
        if record_list:
            content = ";".join(record_list)
            models.AssetRecord.objects.create(asset_obj=server_obj.asset, content=content)
            return render(request, 'asset.html')