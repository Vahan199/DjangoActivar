# Generated by Django 4.0.6 on 2022-07-30 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_aboutqu_numb2_aboutqu_numb3_aboutqu_numb4_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSl2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='img1')),
            ],
            options={
                'verbose_name': 'AboutSl1',
                'verbose_name_plural': 'AboutSls2',
            },
        ),
        migrations.RemoveField(
            model_name='aboutsl',
            name='img2',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='name3',
            field=models.TextField(null=True, verbose_name='Us text2'),
        ),
    ]
