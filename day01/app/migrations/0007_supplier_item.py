# Generated by Django 5.0.7 on 2024-08-02 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='item',
            field=models.ManyToManyField(to='app.item'),
        ),
    ]