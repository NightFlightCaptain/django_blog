# Generated by Django 2.1.8 on 2020-05-28 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0002_auto_20200528_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_on',
            field=models.DateTimeField(auto_now=True, db_column='created_on'),
        ),
    ]