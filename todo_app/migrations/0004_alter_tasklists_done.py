# Generated by Django 4.2.2 on 2023-07-05 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_tasklists_manage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklists',
            name='done',
            field=models.BooleanField(default=True),
        ),
    ]
