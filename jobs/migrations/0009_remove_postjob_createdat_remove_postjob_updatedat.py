# Generated by Django 5.0.1 on 2024-03-05 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_delete_customuser_postjob_joblocationtype_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postjob',
            name='createdAt',
        ),
        migrations.RemoveField(
            model_name='postjob',
            name='updatedAt',
        ),
    ]