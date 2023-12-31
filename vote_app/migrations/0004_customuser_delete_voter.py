# Generated by Django 4.1.3 on 2023-04-04 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote_app', '0003_voter'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('state', models.CharField(max_length=100)),
                ('local_government', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('secondname', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='voter',
        ),
    ]
