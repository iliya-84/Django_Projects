# Generated by Django 3.2.5 on 2021-08-16 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20210812_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='title',
            field=models.CharField(choices=[('MR', 'Mr.'), ('MRS', 'Mrs.'), ('MS', 'Ms.')], max_length=3),
        ),
    ]
