# Generated by Django 4.0.4 on 2024-05-09 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biryani', '0003_remove_biryanidb_id_alter_biryanidb_biryani_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='biryanidb',
            name='biryani_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='biryani_images/'),
        ),
    ]
