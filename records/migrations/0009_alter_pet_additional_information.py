# Generated by Django 4.2.17 on 2024-12-28 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0008_pet_additional_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='additional_information',
            field=models.TextField(blank=True, null=True),
        ),
    ]