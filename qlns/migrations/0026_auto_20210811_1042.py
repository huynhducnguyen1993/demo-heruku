# Generated by Django 3.2.3 on 2021-08-11 03:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('qlns', '0025_giaichi_trangthaiduyet_tckt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giaichi',
            name='guiduyet',
            field=models.CharField(choices=[('0', 'Gửi Sếp'), ('1', ' Chỉ Gửi Trưởng Phòng'), ('2', ' Tài Chính Kế Toán')], max_length=20, verbose_name='Trạng Thái Gửi Duyệt'),
        ),
        migrations.AlterField(
            model_name='giaichi',
            name='trangthaiduyet_tckt',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]