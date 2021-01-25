# Generated by Django 3.1.5 on 2021-01-22 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_duration_mani'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra', models.CharField(choices=[('NONE', 'None'), ('PLN', 'Peeling'), ('ENT', 'Entfernung fremder Gele oder Shellac'), ('NGL', 'Nagellack'), ('SHL', 'Shellac'), ('SLF', 'Shellac French'), ('AZP', 'Augenbraunen zupfen'), ('AFR', 'Augenbraunen färben'), ('WFR', 'Wimpern färben'), ('OLE', 'Oberlippen Enthaarung'), ('ACE', 'Achsel Enthaarung'), ('KNE', 'Enthaarung der Beine bis zum Knie'), ('BEE', 'Enthaarung der ganzen Beine'), ('RUE', 'Enthaarung des Rückens oder Brust')], default='NONE', max_length=64)),
                ('price', models.PositiveSmallIntegerField()),
                ('duration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.duration')),
            ],
        ),
    ]
