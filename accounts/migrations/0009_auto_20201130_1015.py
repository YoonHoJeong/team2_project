# Generated by Django 2.2.14 on 2020-11-30 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20201130_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='actor',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Actor'),
        ),
        migrations.AlterField(
            model_name='like',
            name='director',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Director'),
        ),
        migrations.AlterField(
            model_name='like',
            name='staff',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Staff'),
        ),
    ]
