# Generated by Django 5.1.5 on 2025-06-24 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emp',
            old_name='workig',
            new_name='working',
        ),
        migrations.AlterField(
            model_name='emp',
            name='department',
            field=models.CharField(max_length=10),
        ),
    ]
