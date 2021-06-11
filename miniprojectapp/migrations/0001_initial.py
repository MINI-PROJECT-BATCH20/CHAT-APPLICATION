# Generated by Django 3.2.3 on 2021-06-03 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=40)),
                ('mail_id', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'signup',
            },
        ),
    ]
