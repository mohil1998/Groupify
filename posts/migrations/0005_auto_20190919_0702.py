# Generated by Django 2.2.5 on 2019-09-19 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20190919_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover_html',
            field=models.ImageField(editable=False, upload_to=''),
        ),
    ]
