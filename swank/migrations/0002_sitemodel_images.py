# Generated by Django 3.0.6 on 2020-06-02 04:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('swank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitemodel',
            name='images',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
