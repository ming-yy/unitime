from mongoengine import Document, ListField


class misAsignaturas(Document):
    misAsignaturas = ListField(required=True)
    