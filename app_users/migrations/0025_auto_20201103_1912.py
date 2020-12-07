# Generated by Django 2.2 on 2020-11-03 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0024_auto_20201101_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='image',
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_users.News')),
            ],
        ),
    ]
