# Generated by Django 5.0.6 on 2024-09-28 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ip_recog', '0003_remove_about_model_image_of_what_about_model_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about_model',
            old_name='image',
            new_name='image_1',
        ),
        migrations.AddField(
            model_name='about_model',
            name='image_2',
            field=models.ImageField(null=True, upload_to='model_evaluate_img/'),
        ),
        migrations.AddField(
            model_name='about_model',
            name='image_3',
            field=models.ImageField(null=True, upload_to='model_evaluate_img/'),
        ),
    ]
