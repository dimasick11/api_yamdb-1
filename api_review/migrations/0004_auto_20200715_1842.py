# Generated by Django 3.0.5 on 2020-07-15 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_review', '0003_auto_20200715_1840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='review_id',
            new_name='review',
        ),
    ]
