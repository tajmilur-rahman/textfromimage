# Generated by Django 4.2 on 2023-04-17 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translator_app', '0003_alter_translate_from_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translate',
            name='from_language',
            field=models.CharField(choices=[('EN', 'English'), ('FR', 'French'), ('ES', 'Spanish'), ('ZH', 'Chinese')], help_text='Enter the source language.', max_length=500),
        ),
        migrations.AlterField(
            model_name='translate',
            name='text',
            field=models.TextField(help_text='Enter the text to be translated.'),
        ),
        migrations.AlterField(
            model_name='translate',
            name='to_language',
            field=models.CharField(choices=[('EN', 'English'), ('FR', 'French'), ('ES', 'Spanish'), ('ZH', 'Chinese')], help_text='Enter the target language.', max_length=500),
        ),
        migrations.AlterField(
            model_name='translate',
            name='translation',
            field=models.TextField(blank=True, editable=False, help_text='The translated text.', null=True),
        ),
    ]