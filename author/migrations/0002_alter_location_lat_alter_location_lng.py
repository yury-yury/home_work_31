# Generated by Django 4.1.7 on 2023-03-17 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.DecimalField(decimal_places=6, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='lng',
            field=models.DecimalField(decimal_places=6, max_digits=10, null=True),
        ),
    ]