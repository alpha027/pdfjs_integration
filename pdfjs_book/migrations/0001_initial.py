# Generated by Django 3.0.5 on 2020-11-16 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('doc_type', models.CharField(max_length=50)),
                ('pages', models.PositiveIntegerField()),
                ('authors', models.CharField(blank=True, max_length=50)),
                ('journal', models.CharField(blank=True, max_length=70)),
                ('ISBN', models.CharField(blank=True, max_length=20)),
                ('readers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
