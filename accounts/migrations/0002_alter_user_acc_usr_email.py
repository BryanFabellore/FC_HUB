# Generated by Django 4.1.5 on 2023-01-19 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_acc',
            name='usr_email',
            field=models.EmailField(max_length=250),
        ),
    ]