# Generated by Django 4.0.6 on 2022-08-07 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_gallery_name_gallery_name2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='logo')),
            ],
            options={
                'verbose_name': 'Logo',
                'verbose_name_plural': 'Logos',
            },
        ),
        migrations.CreateModel(
            name='Logo2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='logo')),
            ],
            options={
                'verbose_name': 'Logo2',
                'verbose_name_plural': 'Logos2',
            },
        ),
        migrations.CreateModel(
            name='Logo3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='Logo')),
            ],
            options={
                'verbose_name': 'Logo3',
                'verbose_name_plural': 'Logos3',
            },
        ),
        migrations.CreateModel(
            name='Logo4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='logo')),
            ],
            options={
                'verbose_name': 'Logo4',
                'verbose_name_plural': 'Logos4',
            },
        ),
        migrations.AlterField(
            model_name='blogdet3',
            name='name',
            field=models.CharField(max_length=190, null=True, verbose_name='name1'),
        ),
        migrations.AlterField(
            model_name='blogdet3',
            name='name2',
            field=models.CharField(max_length=190, null=True, verbose_name='name2'),
        ),
    ]