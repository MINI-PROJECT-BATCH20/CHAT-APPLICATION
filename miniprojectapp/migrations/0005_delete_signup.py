# Generated by Django 3.2.3 on 2021-06-09 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniprojectapp', '0004_rename_user_id_signup_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Signup',
        ),
    ]
