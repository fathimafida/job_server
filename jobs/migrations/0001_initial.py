# Generated by Django 4.2.2 on 2024-02-04 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('companyName', models.CharField(max_length=255)),
            ],
        ),
    ]