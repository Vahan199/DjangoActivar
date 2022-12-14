# Generated by Django 4.0.6 on 2022-08-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_scour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=40, verbose_name='blog name1')),
                ('name2', models.CharField(max_length=40, verbose_name='blog name2')),
                ('img', models.ImageField(upload_to='media', verbose_name='blog img')),
            ],
            options={
                'verbose_name': 'Blog1',
                'verbose_name_plural': 'Blog1s',
            },
        ),
        migrations.CreateModel(
            name='Blog2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=40, verbose_name='blog2 name1')),
                ('name2', models.CharField(max_length=40, verbose_name='blog2 name2')),
                ('img', models.ImageField(upload_to='media', verbose_name='blog2 img')),
            ],
            options={
                'verbose_name': 'Blog2',
                'verbose_name_plural': 'Blog2s',
            },
        ),
    ]
