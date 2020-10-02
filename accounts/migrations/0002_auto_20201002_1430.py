# Generated by Django 2.2.14 on 2020-10-02 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='intro',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name_eng',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
