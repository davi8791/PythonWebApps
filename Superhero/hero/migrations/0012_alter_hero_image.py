# Generated by Django 4.1 on 2022-11-22 19:53

from django.db import migrations, models
import hero.models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0011_rename_author_investigator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=hero.models.get_upload),
        ),
    ]
