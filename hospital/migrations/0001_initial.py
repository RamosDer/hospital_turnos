# Generated by Django 4.2.4 on 2023-08-14 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('edad', models.PositiveIntegerField()),
                ('embarazada', models.BooleanField(default=False)),
                ('tercera_edad', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('especialidad', models.CharField(max_length=100)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital')),
            ],
        ),
    ]
