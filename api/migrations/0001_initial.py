# Generated by Django 2.2.6 on 2019-11-03 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=30)),
                ('courses', models.CharField(max_length=10)),
            ],
        ),
    ]
