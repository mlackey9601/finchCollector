# Generated by Django 3.0.2 on 2020-03-17 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feeding'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sighting',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='sighting',
            name='date',
            field=models.DateField(verbose_name='sighting date'),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='spot',
            field=models.CharField(choices=[('M', 'Morning'), ('E', 'Evening'), ('N', 'Night')], default='M', max_length=1),
        ),
    ]
