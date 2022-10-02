from django.forms import ModelForm
from .models import Curso, Estudiante, Prueba, Preguntas, EstudiantePreguntas, Tema

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = ('nombres','apellidos','nombre_completo',)   

class UEstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = ('curso','nombres','apellidos','nombre_completo',)             

class EstudiantePreguntasForm(ModelForm):
    class Meta:
        model = EstudiantePreguntas
        fields = ('estudiante','correcto',)       

class PruebaForm(ModelForm):
    class Meta:
        model = Prueba
        fields = ('nombre_prueba',)

class PreguntasForm(ModelForm):

    class Meta:
        model = Preguntas
        fields = ('tema', 'pregunta',)

class UPreguntasForm(ModelForm):

    class Meta:
        model = Preguntas
        fields = ('pregunta',)

class TemaForm(ModelForm):
    class Meta:
        model = Tema
        fields = ('nombre_tema',)
