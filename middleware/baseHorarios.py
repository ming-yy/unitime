from db.daos.userDao import user_dao
from db.daos.carreraDao import carrera_dao
from db.daos.asignaturaDao import asignatura_dao
from db.daos.grupoDao import grupo_dao
from db.daos.misAsignaturasDao import misAsignaturas_dao
from db.daos.horarioDao import horario_dao
from db.models.user import User


def get_usuario(email):
    return user_dao.get_by_email(email)

def get_carrera(name):
    return carrera_dao.get_carrera_by_name(name)

def get_asignatura(carreraCod):
   return asignatura_dao.get_asignatura_by_carrera(carreraCod)

def get_asignatura_by_codeId(codigo):
    return asignatura_dao.get_asignatura_by_code(codigo)

def get_asignatura_carrera_curso_semestre(name, curso, semestre):
   return asignatura_dao.get_asignatura(name, curso, semestre)

def get_grupo_carrera_curso(name, curso):
   return grupo_dao.get_grupo(name, curso)

def get_numCursos(name):
    return carrera_dao.get_numCursos_by_name(name)

def add_misAsignaturas(misAsignaturas):
    return misAsignaturas_dao.add_misAsignaturas_ids(misAsignaturas)

def add_horario_user(horario):
    return horario_dao.add_horario(horario)

def update_horario(horario,email):
    return user_dao.update_horario_by_email(email,horario)

def get_mi_horario(id):
    return horario_dao.get_horario(id)

def get_misAsig(id):
    return misAsignaturas_dao.get_by_id(id)

def get_asig(id):
    return asignatura_dao.get_asignatura_by_id(id)