# Generated by Django 4.1 on 2022-09-23 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0002_hero_about_1_hero_about_2_hero_about_source_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='image',
            field=models.ImageField(default='', upload_to='static/'),
        ),
    ]
