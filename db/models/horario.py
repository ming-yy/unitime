from mongoengine import Document, StringField, DateTimeField, IntField, ReferenceField
import datetime
from db.models.misAsignaturas import misAsignaturas
import json


class Horario(Document):
    nombre = StringField (max_length=100, required=True)
    misAsignaturas = ReferenceField(misAsignaturas, required=True)
    horaFin= IntField(required=True)
    horaIni= IntField(required=True)
