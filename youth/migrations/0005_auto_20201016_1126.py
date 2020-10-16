# Generated by Django 3.1.2 on 2020-10-16 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('youth', '0004_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='youth.post')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
