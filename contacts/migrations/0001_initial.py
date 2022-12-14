# Generated by Django 4.1.3 on 2022-11-24 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=255)),
                ('message', models.TextField()),
                ('is_responded', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-pub_date'],
                'get_latest_by': 'pub_date',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-pub_date'],
                'get_latest_by': 'pub_date',
            },
        ),
    ]
