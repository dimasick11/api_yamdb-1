# Generated by Django 3.0.5 on 2020-07-15 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_review', '0004_auto_20200715_1842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='review',
            new_name='review_id',
        ),
    ]
