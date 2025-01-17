# Generated by Django 4.1 on 2022-09-23 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='about_1',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='hero',
            name='about_2',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='hero',
            name='about_source',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='hero',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='hero',
            name='primary_rgb',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AddField(
            model_name='hero',
            name='quote',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='hero',
            name='real_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='hero',
            name='strengths',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='hero',
            name='weaknesses',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='hero',
            name='hero_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
