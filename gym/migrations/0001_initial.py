# Generated by Django 3.2 on 2021-04-28 21:22

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('contact', phone_field.models.PhoneField(max_length=31)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('address', models.TextField(null=True)),
                ('aadhar', models.ImageField(blank=True, null=True, upload_to='')),
                ('gender', models.CharField(max_length=20)),
                ('aerobics', models.BooleanField(default=False, verbose_name='Aerobics')),
                ('yoga', models.BooleanField(default=False, verbose_name='Yoga')),
                ('weight_training', models.BooleanField(default=False, verbose_name='Weight Training')),
                ('cardio', models.BooleanField(default=False, verbose_name='Cardio')),
                ('timing', models.CharField(choices=[('morning', 'Morning'), ('evening', 'Evening'), ('night', 'Night')], default='Morning', max_length=20)),
                ('weight', models.FloatField()),
                ('dor', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Members',
                'ordering': ['-dor'],
            },
        ),
    ]
