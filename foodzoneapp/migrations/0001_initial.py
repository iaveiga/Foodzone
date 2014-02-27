# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = []

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('descripcion', models.CharField(max_length=50),), ('latitud', models.FloatField(),), ('longitud', models.FloatField(),), ('activo', models.BooleanField(default=True),)],
            bases = (models.Model,),
            options = {},
            name = 'Zona',
        ),
    ]
