# Generated by Django 4.2 on 2024-03-31 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paginas',
            name='title',
            field=models.CharField(max_length=200, verbose_name='titulo'),
        ),
    ]