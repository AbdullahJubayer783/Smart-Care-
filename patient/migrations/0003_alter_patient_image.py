# Generated by Django 4.2.7 on 2024-03-20 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_alter_patient_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='image',
            field=models.ImageField(upload_to='patient/media/userimage/'),
        ),
    ]
