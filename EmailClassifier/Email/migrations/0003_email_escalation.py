# Generated by Django 5.0.6 on 2024-05-29 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Email', '0002_email_from_email_to_alter_email_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='escalation',
            field=models.TextField(default='None'),
            preserve_default=False,
        ),
    ]