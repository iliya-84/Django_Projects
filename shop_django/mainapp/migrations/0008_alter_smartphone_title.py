# Generated by Django 3.2.5 on 2021-08-16 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_alter_smartphone_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Наименование'),
        ),
    ]