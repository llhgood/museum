# Generated by Django 3.2.12 on 2023-04-08 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yn_museum', '0008_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='notes',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='备注'),
        ),
    ]