# Generated by Django 3.1.2 on 2020-10-22 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20201022_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='types',
            field=models.CharField(default='donations', max_length=100, null=True),
        ),
    ]