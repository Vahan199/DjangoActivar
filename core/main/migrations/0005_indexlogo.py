# Generated by Django 4.0.6 on 2022-07-30 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_indexblog_indexchoos_indexplan_indexplan2m_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='logo')),
            ],
            options={
                'verbose_name': 'IndexLogo',
                'verbose_name_plural': 'IndexSLogo',
            },
        ),
    ]
