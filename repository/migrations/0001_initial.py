# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-17 08:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='\u7528\u6237\u540d')),
                ('password', models.CharField(max_length=32, verbose_name='\u7528\u6237\u540d')),
            ],
            options={
                'verbose_name_plural': '\u7ba1\u7406\u4eba\u5458\u8868',
            },
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_type_id', models.IntegerField(choices=[(1, '\u670d\u52a1\u5668'), (2, '\u4ea4\u6362\u673a'), (3, '\u9632\u706b\u5899')], default=1)),
                ('device_status_id', models.IntegerField(choices=[(1, '\u4e0a\u67b6'), (2, '\u5728\u7ebf'), (3, '\u79bb\u7ebf'), (4, '\u4e0b\u67b6')], default=1)),
                ('cabinet_num', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u673a\u67dc\u53f7')),
                ('cabinet_order', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u673a\u67dc\u4e2d\u5e8f\u53f7')),
                ('latest_date', models.DateField(null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '\u8d44\u4ea7\u8868',
            },
        ),
        migrations.CreateModel(
            name='AssetRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('asset_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ar', to='repository.Asset')),
            ],
            options={
                'verbose_name_plural': '\u8d44\u4ea7\u8bb0\u5f55\u8868',
            },
        ),
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='\u4e1a\u52a1\u7ebf')),
            ],
            options={
                'verbose_name_plural': '\u4e1a\u52a1\u7ebf',
            },
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(max_length=5, verbose_name='\u63d2\u69fd')),
                ('model', models.CharField(max_length=32, verbose_name='\u786c\u76d8\u578b\u53f7')),
                ('capacity', models.CharField(max_length=32, verbose_name='\u78c1\u76d8\u5bb9\u91cf')),
                ('pd_type', models.CharField(max_length=32, verbose_name='\u78c1\u76d8\u7c7b\u578b')),
            ],
            options={
                'verbose_name_plural': '\u786c\u76d8\u8868',
            },
        ),
        migrations.CreateModel(
            name='ErrorLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16)),
                ('content', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('asset_obj', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='repository.Asset')),
            ],
            options={
                'verbose_name_plural': '\u9519\u8bef\u65e5\u5fd7\u8868',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u673a\u623f')),
                ('floor', models.CharField(default=1, max_length=32, verbose_name='\u697c\u5c42')),
            ],
            options={
                'verbose_name_plural': '\u673a\u623f',
            },
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(max_length=32, verbose_name='\u63d2\u69fd')),
                ('manufacturer', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u5236\u9020\u5546')),
                ('model', models.CharField(max_length=64, verbose_name='\u578b\u53f7')),
                ('capacity', models.CharField(max_length=32, verbose_name='\u5bb9\u91cf')),
                ('sn', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u5185\u5b58SN\u53f7')),
                ('speed', models.CharField(blank=True, max_length=16, null=True, verbose_name='\u901f\u5ea6')),
            ],
            options={
                'verbose_name_plural': '\u5185\u5b58\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('management_ip', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u7ba1\u7406IP')),
                ('vlan_ip', models.CharField(blank=True, max_length=64, null=True, verbose_name='VlanIP')),
                ('intranet_ip', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u5185\u7f51IP')),
                ('sn', models.CharField(max_length=64, unique=True, verbose_name='SN\u53f7')),
                ('manufacture', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u5236\u9020\u5546')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u578b\u53f7')),
                ('port_num', models.SmallIntegerField(blank=True, null=True, verbose_name='\u7aef\u53e3\u4e2a\u6570')),
                ('device_detail', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u8bbe\u7f6e\u8be6\u7ec6\u914d\u7f6e')),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='repository.Asset')),
            ],
            options={
                'verbose_name_plural': '\u7f51\u7edc\u8bbe\u5907',
            },
        ),
        migrations.CreateModel(
            name='NIC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='\u7f51\u5361\u540d')),
                ('hwaddr', models.CharField(max_length=64, verbose_name='\u7f51\u5361mac\u5730\u5740')),
                ('netmask', models.CharField(max_length=64)),
                ('ipaddrs', models.CharField(max_length=256, verbose_name='ip\u5730\u5740')),
                ('up', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': '\u7f51\u5361\u8868',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=64, unique=True)),
                ('sn', models.CharField(db_index=True, max_length=64, verbose_name='\u4e3b\u677fSN\u53f7')),
                ('manufacturer', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u5236\u9020\u5546')),
                ('model', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u578b\u53f7')),
                ('manage_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='\u7ba1\u7406IP')),
                ('os_platform', models.CharField(blank=True, max_length=16, null=True, verbose_name='\u7cfb\u7edf')),
                ('os_version', models.CharField(blank=True, max_length=16, null=True, verbose_name='\u7cfb\u7edf\u7248\u672c')),
                ('cpu_count', models.IntegerField(blank=True, null=True, verbose_name='CPU\u4e2a\u6570')),
                ('cpu_physical_count', models.IntegerField(blank=True, null=True, verbose_name='CPU\u7269\u7406\u4e2a\u6570')),
                ('cpu_model', models.CharField(blank=True, max_length=128, null=True, verbose_name='CPU\u578b\u53f7')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='repository.Asset')),
            ],
            options={
                'verbose_name_plural': '\u670d\u52a1\u5668\u8868',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='\u8d44\u4ea7\u6807\u7b7e')),
            ],
            options={
                'verbose_name_plural': '\u6807\u7b7e\u8868',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u5de5\u4f5c\u7ec4')),
            ],
            options={
                'verbose_name_plural': '\u4eba\u5458\u5206\u914d\u8868',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u59d3\u540d')),
                ('email', models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1')),
                ('phone', models.CharField(max_length=32, verbose_name='\u5ea7\u673a')),
                ('mobile', models.CharField(max_length=32, verbose_name='\u624b\u673a')),
            ],
            options={
                'verbose_name_plural': '\u7528\u6237\u8868',
            },
        ),
        migrations.AddField(
            model_name='usergroup',
            name='users',
            field=models.ManyToManyField(to='repository.UserProfile'),
        ),
        migrations.AddField(
            model_name='nic',
            name='server_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nic', to='repository.Server'),
        ),
        migrations.AddField(
            model_name='memory',
            name='server_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memory', to='repository.Server'),
        ),
        migrations.AddField(
            model_name='disk',
            name='server_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disk', to='repository.Server'),
        ),
        migrations.AddField(
            model_name='businessunit',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='c', to='repository.UserGroup', verbose_name='\u4e1a\u52a1\u8054\u7cfb\u4eba'),
        ),
        migrations.AddField(
            model_name='businessunit',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='m', to='repository.UserGroup', verbose_name='\u7cfb\u7edf\u7ba1\u7406\u5458'),
        ),
        migrations.AddField(
            model_name='assetrecord',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='repository.UserProfile'),
        ),
        migrations.AddField(
            model_name='asset',
            name='business_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='repository.BusinessUnit', verbose_name='\u6240\u5c5e\u4e1a\u52a1\u7ebf'),
        ),
        migrations.AddField(
            model_name='asset',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='repository.IDC', verbose_name='IDC'),
        ),
        migrations.AddField(
            model_name='asset',
            name='tag',
            field=models.ManyToManyField(to='repository.Tag'),
        ),
        migrations.AddField(
            model_name='admininfo',
            name='user_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='repository.UserProfile'),
        ),
    ]