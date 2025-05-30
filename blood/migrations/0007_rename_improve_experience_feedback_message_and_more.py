# Generated by Django 5.2 on 2025-04-25 08:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0006_alter_contact_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='improve_experience',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='age_range',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='donate_next_year',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='first_time_donator',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='improve_utilization',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='inspiration_to_donate',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='process_easy',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='recommend_to_others',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='time_to_contact',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='where_heard_about_us',
        ),
        migrations.AddField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5),
        ),
        migrations.AddField(
            model_name='feedback',
            name='submitted_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
