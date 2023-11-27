from mongoengine import Document, ListField


class Semana(Document):
    dias = ListField(required=True)