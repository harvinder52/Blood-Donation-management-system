# Generated by Django 5.2 on 2025-04-25 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0005_contact_message_contact_submitted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
