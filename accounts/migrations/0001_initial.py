# Generated by Django 2.2.14 on 2020-10-05 23:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(default='', max_length=20)),
                ('name_eng', models.CharField(blank=True, default='', max_length=20)),
                ('age', models.PositiveIntegerField(null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='image/avatar')),
                ('intro', models.TextField(default='')),
                ('education', models.CharField(blank=True, max_length=20, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company', models.CharField(max_length=30)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('weight', models.PositiveIntegerField(blank=True, null=True)),
                ('favorite_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('specialty', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('awards', models.TextField()),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('role', models.CharField(max_length=30)),
                ('tool_list', models.CharField(max_length=200)),
            ],
        ),
    ]
