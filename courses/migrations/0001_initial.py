# Generated by Django 2.0.4 on 2018-04-18 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('docente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Curso Superior')),
                ('date_start', models.DateField(verbose_name='Fecha Inicio')),
                ('date_end', models.DateField(verbose_name='Fecha Fin')),
                ('hours', models.IntegerField(verbose_name='Nro de Horas')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='docente.Docente')),
            ],
            options={
                'verbose_name': 'Curso Superior',
                'verbose_name_plural': 'Cursos Superiores',
            },
        ),
    ]
