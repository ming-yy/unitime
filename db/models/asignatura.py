from mongoengine import Document, StringField, IntField, ReferenceField
from db.models.carrera import Carrera
from db.models.semana import Semana


class Asignatura(Document):
    codigo = IntField(unique=True, required=True)
    nombre = StringField(max_length=80, required=True)    #Tamaño máximo al nombre? (J)
    semestre = IntField(required=True)
    curso = IntField(required=True)
    horas = ReferenceField(Semana, required=True)
    carrera = ReferenceField(Carrera, required=True)