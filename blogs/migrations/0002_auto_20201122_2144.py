# Generated by Django 3.1.3 on 2020-11-22 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name_plural': 'blog posts'},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='text',
            field=models.TextField(),
        ),
    ]