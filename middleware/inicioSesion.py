from db.daos.userDao import user_dao
from db.models.user import User


def autentificar_usuario(email, contrasenya):
    usuario = user_dao.get_by_email(email)
    if usuario:
        if usuario['password'] == str(contrasenya):
            return True
    return False
