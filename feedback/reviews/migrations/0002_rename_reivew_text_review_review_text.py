# Generated by Django 3.2.3 on 2021-07-07 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='reivew_text',
            new_name='review_text',
        ),
    ]