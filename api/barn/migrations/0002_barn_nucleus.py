# Generated by Django 3.0.6 on 2020-05-12 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('barn', '0001_initial'),
        ('nucleus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='barn',
            name='nucleus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleus.Nucleus'),
        ),
    ]
