# Generated by Django 4.2.6 on 2023-11-19 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_rename_image_books_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='language',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
