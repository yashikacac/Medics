# Generated by Django 3.1.3 on 2020-11-09 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospitals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('Address', models.TextField()),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
            ],
        ),
    ]
