# Generated by Django 3.1.4 on 2021-05-29 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210529_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.CharField(default='fas fa-hand-sparkles', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='service_type',
            field=models.CharField(max_length=50),
        ),
    ]
