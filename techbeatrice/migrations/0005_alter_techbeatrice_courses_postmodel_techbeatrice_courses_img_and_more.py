# Generated by Django 5.0.1 on 2024-07-14 14:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techbeatrice', '0004_rename_techbeatricepostmodel_techbeatrice_courses_postmodel'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='techbeatrice_courses_postmodel',
            name='techbeatrice_courses_img',
            field=models.ImageField(blank=True, null=True, upload_to='tech_courses_img/'),
        ),
        migrations.CreateModel(
            name='Techbeatrice_Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('techbeatrice_subjects_title', models.CharField(blank=True, max_length=205, null=True)),
                ('techbeatrice_subjects_description', models.TextField()),
                ('techbeatrice_subjects_img', models.ImageField(blank=True, null=True, upload_to='tech_subjects_img/')),
                ('techbeatrice_subjects_slug', models.SlugField(blank=True, max_length=205, null=True)),
                ('techbeatrice_subjects_publish_date', models.DateTimeField(auto_now_add=True)),
                ('techbeatrice_subjects_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-techbeatrice_subjects_publish_date'],
            },
        ),
    ]
