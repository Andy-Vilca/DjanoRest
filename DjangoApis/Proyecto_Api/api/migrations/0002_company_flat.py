# Generated by Django 3.2.4 on 2021-07-15 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='flat',
            field=models.CharField(choices=[('A', 'Activo'), ('F', 'Finalizado')], default='A', max_length=1),
        ),
    ]
