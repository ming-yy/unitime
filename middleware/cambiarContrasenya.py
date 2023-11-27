from db.daos.userDao import user_dao

def get_usuario(email):
    return user_dao.get_by_email(email)

def update_password(email, password):
    user_dao.update_password_by_email(email, password)