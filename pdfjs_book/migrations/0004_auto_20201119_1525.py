# Generated by Django 3.0.5 on 2020-11-19 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdfjs_book', '0003_auto_20201117_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='ISBN',
        ),
        migrations.RemoveField(
            model_name='document',
            name='journal',
        ),
        migrations.RemoveField(
            model_name='document',
            name='readers',
        ),
    ]