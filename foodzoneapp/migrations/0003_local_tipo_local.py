# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('foodzoneapp', '0002_local_plato_tipolocal')]

    operations = [
        migrations.AddField(
            field = models.ForeignKey(to=u'foodzoneapp.TipoLocal', default=0, to_field=u'id'),
            preserve_default = False,
            name = 'tipo_local',
            model_name = 'local',
        ),
    ]
