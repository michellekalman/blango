# Generated by Django 3.2.25 on 2024-10-29 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20241029_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='object_id',
            field=models.PositiveIntegerField(db_index=True),
        ),
    ]
