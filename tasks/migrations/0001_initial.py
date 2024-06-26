# Generated by Django 5.0.4 on 2024-05-01 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=44)),
                ('description', models.CharField(max_length=144)),
                ('date', models.DateField()),
                ('duration', models.TimeField()),
                ('status', models.CharField(choices=[('conclude', 'Conclude'), ('pendant', 'Pendant')], default='pendant', max_length=8)),
            ],
        ),
    ]
