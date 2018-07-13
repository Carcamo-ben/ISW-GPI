from django.forms import ModelForm
from .models import *
# Create the form class.
class SOLICITUDESForm(ModelForm):
	class Meta:
		model = SOLICITUDES
		fields = ['Fecha_Vigencia', 'Version', 'Estado', 'Centro_de_Costo',
		'Documento','Solicitado_por','Fecha_Solicitud','Fecha_Requerida'
		]


#,'CC','Sol','Item','Descripcion','Cant','Unid','Cert','AoD' 