from mongoengine import Document, StringField, IntField
import json


class HorasAsignatura(Document):
    tipo = StringField(required=True)
    dia = StringField(required=True)
    horaInicio = IntField(required=True)
    horaFin = IntField(required=True)