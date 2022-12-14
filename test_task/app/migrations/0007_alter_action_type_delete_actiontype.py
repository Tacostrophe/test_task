# Generated by Django 4.1 on 2022-08-24 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_actiontype_alter_action_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='type',
            field=models.CharField(choices=[('r', 'read'), ('c', 'create'), ('u', 'update'), ('d', 'delete')], default='r', max_length=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ActionType',
        ),
    ]
