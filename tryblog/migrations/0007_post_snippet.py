# Generated by Django 4.0.2 on 2022-02-25 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tryblog', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Read More', max_length=255),
        ),
    ]