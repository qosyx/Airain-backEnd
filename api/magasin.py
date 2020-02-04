import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'database'))
import dbmagasin as p
# import database as database
# from database import connexion as connexion
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
path = path+"/connectParameters.json"



def createMagasin(magasinJson):
    try:
        result = p.createMagasin(path,magasinJson)
        return result
    except print(0):
        pass


def updateMagasin(magasinJson,magasinId):
    result = p.updateMagasin(path, magasinJson,magasinId)
    return result

def deleteMagasin(magasinId):
    result = p.deleteMagasin(path, magasinId)
    return result
def getAllMagasin():
    result = p.getAllMagasin(path)
    return result
def getMagasinByCriteria(magasinJson):
    try:
        result = p.getMagasinByCriteria(path,magasin)
        return result
    except print(0):
        pass
