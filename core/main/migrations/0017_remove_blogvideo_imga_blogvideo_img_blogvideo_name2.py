# Generated by Django 4.0.6 on 2022-08-07 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_logo_logo2_logo3_logo4_alter_blogdet3_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogvideo',
            name='imga',
        ),
        migrations.AddField(
            model_name='blogvideo',
            name='img',
            field=models.ImageField(null=True, upload_to='media', verbose_name='videp img'),
        ),
        migrations.AddField(
            model_name='blogvideo',
            name='name2',
            field=models.CharField(max_length=80, null=True, verbose_name='video name2'),
        ),
    ]