# Generated by Django 4.2 on 2023-05-01 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cadastros', '0002_exercicio_grupomuscular_treino_treinoaluno_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercicio',
            name='id_GrupoMuscular',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treinoaluno',
            name='id_Excecicio',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treinoaluno',
            name='id_GrupoMuscular',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treinoaluno',
            name='id_Treino',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treinoaluno',
            name='id_aluno',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treinoaluno',
            name='qt_peso',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treinoaluno',
            name='qt_repeticoes',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treinoaluno',
            name='qt_series',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
