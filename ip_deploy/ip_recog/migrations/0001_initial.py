# Generated by Django 5.0.6 on 2024-09-28 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_of_what', models.TextField(max_length=20)),
                ('image', models.ImageField(null=True, upload_to='foods_img/')),
            ],
        ),
    ]
