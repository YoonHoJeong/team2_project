# Generated by Django 2.2.14 on 2020-11-30 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_merge_20201130_0852'),
        ('accounts', '0013_auto_20201130_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='movie',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Movie'),
        ),
    ]
