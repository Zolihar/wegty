# Generated by Django 4.0.1 on 2022-01-19 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weightloss', '0005_alter_post_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='checklist',
            field=models.CharField(max_length=255),
        ),
    ]
