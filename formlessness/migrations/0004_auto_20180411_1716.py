# Generated by Django 2.0.4 on 2018-04-11 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formlessness', '0003_processing_recipient_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formless',
            old_name='input',
            new_name='input_amount',
        ),
        migrations.RenameField(
            model_name='formless',
            old_name='output',
            new_name='output_amount',
        ),
    ]