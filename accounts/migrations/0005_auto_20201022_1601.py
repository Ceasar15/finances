# Generated by Django 3.1.2 on 2020-10-22 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201022_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='types',
            field=models.CharField(choices=[('dues', 'Dues'), ('welfare', 'Selfare'), ('special', 'Special'), ('donations', 'Donations')], default='donations', max_length=100, null=True),
        ),
    ]
