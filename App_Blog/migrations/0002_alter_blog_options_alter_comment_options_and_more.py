# Generated by Django 4.1.7 on 2023-07-22 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-publish_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(default='-'),
            preserve_default=False,
        ),
    ]
