from mongoengine import Document, StringField, IntField
import json


class Carrera(Document):
    codigo = StringField(unique=True, required=True)
    nombre = StringField(max_length=80, required=True)
    numCursos = IntField(required=True)