# Generated by Django 2.2.2 on 2019-07-08 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190708_1550'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-publish_date', '-updated', '-timestamp']},
        ),
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
