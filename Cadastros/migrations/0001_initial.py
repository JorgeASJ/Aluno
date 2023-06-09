# Generated by Django 4.1.7 on 2023-02-18 23:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id_Aluno', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Nome', models.CharField(max_length=255)),
                ('Idade', models.IntegerField()),
                ('Peso', models.FloatField()),
                ('Altura', models.FloatField()),
                ('Contato', models.CharField(max_length=255)),
                ('Objetivo', models.CharField(max_length=255)),
                ('dt_Cadasto', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
