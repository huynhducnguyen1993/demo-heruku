# Generated by Django 3.2.3 on 2021-07-21 10:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('qlns', '0018_alter_dexuat_hangmuc'),
    ]

    operations = [
        migrations.AddField(
            model_name='giaichi',
            name='hangmuc',
            field=models.CharField(choices=[('0', 'Hàng Hóa'), ('1', 'Mua Sắm Thiết Bị'), ('2', 'Khác')], default="", max_length=20, verbose_name='Hạng Mục'),
            preserve_default=False,
        ),
    ]