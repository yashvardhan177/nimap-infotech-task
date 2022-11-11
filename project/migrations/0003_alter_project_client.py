# Generated by Django 3.2.16 on 2022-11-10 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_remove_client_projects'),
        ('project', '0002_project_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_client', to='client.client'),
        ),
    ]