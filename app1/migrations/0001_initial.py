# Generated by Django 4.1.3 on 2022-11-21 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(max_length=150, null=True, unique=True)),
                ('phone_no', models.IntegerField(max_length=12, unique=True)),
            ],
        ),
    ]
