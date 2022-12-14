# Generated by Django 4.1 on 2022-08-24 11:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_action_session_session_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('r', 'read'), ('c', 'create'), ('u', 'update'), ('d', 'delete')], max_length=1, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='action',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='app.actiontype'),
        ),
    ]
