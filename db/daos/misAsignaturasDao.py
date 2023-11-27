from db.models.misAsignaturas import misAsignaturas
from db.daos.daoFactory import misAsignaturas_collection
from bson.objectid import ObjectId
#from app.db import session

class misAsignaturasDAO:
    def __init__(self, model):
        self.model = model    
    
    def get_all(self):
        return misAsignaturas_collection.find()

    def add_misAsignaturas_ids(self, misAsignaturas):
        res = misAsignaturas_collection.insert_one(misAsignaturas.to_mongo().to_dict())
        return res.inserted_id

    def get_by_id(self, id):
        return misAsignaturas_collection.find_one({"_id": ObjectId(str(id))})


#  Singleton object for dao instance
misAsignaturas_dao = misAsignaturasDAO(misAsignaturas)