# Generated by Django 3.2.3 on 2021-07-19 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qlns', '0013_alter_giaichi_dexuat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chucvu_congviec',
            name='tencongviec',
            field=models.CharField(default='', max_length=255, verbose_name='Tên Công việc+ Chúc Vụ'),
        ),
    ]
