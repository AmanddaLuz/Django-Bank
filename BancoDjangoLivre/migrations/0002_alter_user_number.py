# Generated by Django 3.2.9 on 2021-11-29 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BancoDjangoLivre', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.UUIDField(),
        ),
    ]
