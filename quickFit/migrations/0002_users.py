# Generated by Django 4.1.1 on 2022-09-26 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickFit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
