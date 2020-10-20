# Generated by Django 3.1.1 on 2020-10-20 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='acc',
            new_name='tr_acc',
        ),
        migrations.AddField(
            model_name='data',
            name='val_acc',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]