# Generated by Django 5.0.4 on 2024-06-12 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('sname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('sprincy', models.CharField(max_length=50)),
                ('spno', models.CharField(max_length=50)),
                ('saddress', models.CharField(max_length=50)),
            ],
        ),
    ]
