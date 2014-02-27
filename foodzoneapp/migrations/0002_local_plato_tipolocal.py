# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('foodzoneapp', '0001_initial')]

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('descripcion', models.CharField(max_length=60),)],
            bases = (models.Model,),
            options = {},
            name = 'TipoLocal',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('nombre', models.CharField(max_length=30),), ('direccion', models.CharField(max_length=50, blank=True),), ('resena', models.CharField(max_length=60, blank=True),), ('latitud', models.FloatField(),), ('longitud', models.FloatField(),), ('activo', models.BooleanField(default=True),), ('up', models.IntegerField(default=0),), ('down', models.IntegerField(default=0),), ('fechaIngreso', models.DateTimeField(verbose_name='Fecha de Ingreso'),), ('userIngreso', models.IntegerField(),)],
            bases = (models.Model,),
            options = {},
            name = 'Local',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('nombre', models.CharField(max_length=30),), ('descripcion', models.CharField(max_length=50),), ('up', models.IntegerField(default=0),), ('down', models.IntegerField(default=0),), ('fechaIngreso', models.DateTimeField(verbose_name='Fecha de Ingreso'),), ('precio', models.FloatField(),), ('id_local', models.ForeignKey(to=u'foodzoneapp.Local', to_field=u'id'),)],
            bases = (models.Model,),
            options = {},
            name = 'Plato',
        ),
    ]
