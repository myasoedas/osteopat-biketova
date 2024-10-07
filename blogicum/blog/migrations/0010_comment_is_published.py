# Generated by Django 3.2.16 on 2024-09-10 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_published',
            field=models.BooleanField(default=True, help_text='Снимите галочку, чтобы скрыть комментарий.', verbose_name='Опубликовано'),
        ),
    ]
