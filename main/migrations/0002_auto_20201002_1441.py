# Generated by Django 2.2.14 on 2020-10-02 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='festival',
            old_name='festival_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='festival',
            old_name='festival_year',
            new_name='year',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='title_kor',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='section',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
