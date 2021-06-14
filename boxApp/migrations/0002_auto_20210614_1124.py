# Generated by Django 3.2.4 on 2021-06-14 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boxApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pc',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boxApp.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boxApp.producttype'),
        ),
    ]