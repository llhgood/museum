# Generated by Django 3.2.12 on 2023-04-08 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yn_museum', '0006_order_idnumber2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=16, verbose_name='预约类型')),
            ],
            options={
                'verbose_name': '预约类型',
                'verbose_name_plural': '预约类型',
            },
        ),
    ]
