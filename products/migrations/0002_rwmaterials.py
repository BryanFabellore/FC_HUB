# Generated by Django 4.1.5 on 2023-01-24 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='rwMaterials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rwMaterials_name', models.CharField(max_length=250)),
                ('rwMaterials_qty', models.IntegerField()),
                ('rwMaterials_type', models.CharField(max_length=250)),
                ('rwMaterials_size', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
