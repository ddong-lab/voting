# Generated by Django 3.2.5 on 2021-07-07 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='c_grade',
            field=models.IntegerField(default=6),
        ),
        migrations.AddField(
            model_name='candidate',
            name='c_no',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='student',
            name='s_grade',
            field=models.IntegerField(default=6),
        ),
    ]
