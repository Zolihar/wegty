# Generated by Django 4.0.1 on 2022-01-18 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weightloss', '0002_post_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='checklist',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
