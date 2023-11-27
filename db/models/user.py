from mongoengine import Document, StringField, EmailField, BooleanField, ListField


class User(Document):
    email = EmailField(unique=True, required=True)
    username = StringField(max_length=80, unique=True, required=True)
    soyAdmin = BooleanField(default=False)  # Puedes establecer el valor predeterminado según tus necesidades
    password = StringField(required=True)
    horarios = ListField(default=[])