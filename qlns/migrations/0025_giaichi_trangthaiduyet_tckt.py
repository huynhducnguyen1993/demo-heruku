# Generated by Django 3.2.3 on 2021-08-10 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qlns', '0024_giaichi_noidungthanhtoan'),
    ]

    operations = [
        migrations.AddField(
            model_name='giaichi',
            name='trangthaiduyet_tckt',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]