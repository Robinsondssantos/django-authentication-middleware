# Generated by Django 3.0.6 on 2020-05-12 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('integrator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('integrator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integrator.Integrator')),
            ],
        ),
    ]
