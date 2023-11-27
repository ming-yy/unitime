from mongoengine import Document, StringField, IntField
import json


class Grupo(Document):
    codigo = StringField(unique=True, required=True)
    horaInicio = IntField(required=True)
    horaFin = IntField(required=True)