# Generated by Django 3.0.6 on 2020-05-12 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('barn', '0002_barn_nucleus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('barn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barn.Barn')),
            ],
        ),
    ]
