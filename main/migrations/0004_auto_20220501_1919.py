# Generated by Django 3.2.8 on 2022-05-01 23:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_user_userdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountdetails',
            old_name='title',
            new_name='logindetail',
        ),
        migrations.AddField(
            model_name='accountdetails',
            name='website',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
