# Generated by Django 4.1.7 on 2023-06-27 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_remove_histroy_book_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='histroy',
            name='book_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
