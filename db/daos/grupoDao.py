from db.models import grupo
#from app.db import session
from db.daos.daoFactory import grupos_collection
from db.daos.carreraDao import carrera_dao

class GrupoDAO:
    def __init__(self, model):
        self.model = model    
    
    def add_grupo(self, grupo):
        grupos_collection.insert_one(grupo)
    
    def get_all(self):
        return grupos_collection.find()
    
    def get_grupo(self, name, curso):
        carrera = carrera_dao.get_carrera_by_name(name)
        return grupos_collection.find({'carrera': carrera['_id'], 'anyo': int(curso)})
         
grupo_dao = GrupoDAO(grupo)