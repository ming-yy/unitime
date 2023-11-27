from db.daos.userDao import user_dao

def add_usuario(user):
    return user_dao.add_user(user)

def rmv_usuario(email):
    return user_dao.rmv_user(email)

def get_usuario(email):
    return user_dao.get_by_email(email)