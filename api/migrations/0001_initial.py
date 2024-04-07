# Generated by Django 5.0.2 on 2024-04-05 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('IT', 'IT'), ('NON IT', 'NON IT'), ('Mobile Phones', 'Mobile Phones')], max_length=50)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
