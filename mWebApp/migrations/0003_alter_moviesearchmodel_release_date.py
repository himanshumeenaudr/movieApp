# Generated by Django 4.0.3 on 2022-03-28 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mWebApp', '0002_alter_moviesearchmodel_imdbid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesearchmodel',
            name='release_date',
            field=models.CharField(max_length=100),
        ),
    ]
