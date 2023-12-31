# Generated by Django 5.0 on 2023-12-06 03:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update_at', models.DateTimeField(auto_now=True, null=True)),
                ('locale', models.CharField(default='PT', max_length=6)),
                ('lang', models.CharField(default='-03:00', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('last_password_redefinition_at', models.DateTimeField(blank=True, null=True)),
                ('email_verified', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update_at', models.DateTimeField(auto_now=True, null=True)),
                ('date_limit_to_sign', models.DateTimeField(blank=True, null=True)),
                ('signed', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DocUserApp.company')),
                ('created_by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DocUserApp.user')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='created_by_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DocUserApp.user'),
        ),
    ]
