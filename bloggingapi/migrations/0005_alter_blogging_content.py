# Generated by Django 5.0.6 on 2024-09-22 07:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloggingapi', '0004_alter_blogging_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogging',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]