# Generated by Django 4.0.6 on 2022-07-30 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexBg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='bg name')),
                ('name2', models.TextField(verbose_name='bg text')),
                ('img', models.ImageField(upload_to='media', verbose_name='bg image')),
            ],
            options={
                'verbose_name': 'IndexBg',
                'verbose_name_plural': 'IndexBgs',
            },
        ),
        migrations.CreateModel(
            name='IndexProg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='prog name')),
                ('name2', models.TextField(verbose_name='prog text')),
            ],
            options={
                'verbose_name': 'IndexProg',
                'verbose_name_plural': 'IndexProgs',
            },
        ),
        migrations.CreateModel(
            name='IndexProg2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='prog2 name')),
                ('name2', models.TextField(verbose_name='prog2 text')),
                ('img', models.ImageField(upload_to='media', verbose_name='prog2 img')),
            ],
            options={
                'verbose_name': 'IndexProg2',
                'verbose_name_plural': 'IndexProg2s',
            },
        ),
        migrations.CreateModel(
            name='IndexWelc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='welc name')),
                ('name2', models.CharField(max_length=30, verbose_name='welc name2')),
                ('name3', models.TextField(verbose_name='text name')),
                ('img', models.ImageField(upload_to='media', verbose_name='welc img')),
            ],
            options={
                'verbose_name': 'IndexWelc',
                'verbose_name_plural': 'IndexWelcs',
            },
        ),
    ]
