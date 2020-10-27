# Generated by Django 3.1.2 on 2020-10-27 23:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0008_payments_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
