# Generated by Django 5.1.3 on 2024-11-10 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('PUB', 'PUBLISHED'), ('DRF', 'DRAFT')], default='PUB', max_length=5),
        ),
    ]
