# Generated by Django 3.2.7 on 2021-09-20 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_web_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='git_hub',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
