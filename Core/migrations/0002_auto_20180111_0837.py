# Generated by Django 2.0 on 2018-01-11 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitation',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
