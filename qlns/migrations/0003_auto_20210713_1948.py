# Generated by Django 3.2.3 on 2021-07-13 12:48

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qlns', '0002_dexuat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dexuat',
            options={'verbose_name': 'FORM ĐỀ XUẤT', 'verbose_name_plural': 'ĐỀ XUẤT'},
        ),
        migrations.RemoveField(
            model_name='dexuat',
            name='file',
        ),
        migrations.AddField(
            model_name='dexuat',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='filedexuat/'),
        ),
        migrations.AddField(
            model_name='dexuat',
            name='hangmuc',
            field=models.CharField(choices=[('0', 'Hàng Hóa'), ('1', 'Mua Sắm Thiết Bị'), ('2', 'Sự Kiện')], default=django.utils.timezone.now, max_length=20, verbose_name='Trạng Thái Gửi Duyệt'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dexuat',
            name='kinhphi',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dexuat',
            name='username',
            field=models.ForeignKey(default="", on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dexuat',
            name='guiduyet',
            field=models.CharField(choices=[('0', 'Gửi Sếp'), ('1', ' Chỉ Gửi Trưởng Phòng')], max_length=20, verbose_name='Trạng Thái Gửi Duyệt'),
        ),
        migrations.AlterField(
            model_name='dexuat',
            name='noidung',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
