# Generated by Django 4.1.7 on 2023-06-20 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField(max_length=10)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to=models.BigIntegerField(max_length=10))),
            ],
        ),
    ]
