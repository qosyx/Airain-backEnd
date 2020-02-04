import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'database'))
import dbtypepersonnel as p
# import database as database
# from database import connexion as connexion
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
path = path+"/connectParameters.json"



def createtypepersonnel(typepersonnelJson):
    result = p.createTypepersonnel(path,typepersonnelJson)
    return result

def updatetypepersonnel(typepersonnelJson,typepersonnelId):
    result = p.updateTypepersonnel(path, typepersonnelJson,typepersonnelId)
    return result

def deletetypepersonnel(typepersonnelId):
    result = p.deleteTypepersonnel(path, typepersonnelId)
    return result
def getAlltypepersonnel():
    result = p.getAllTypepersonnel(path)
    return result
def gettypepersonnelByCriteria(typepersonnelJson):
    result = p.getTypepersonnelByCriteria(path,typepersonnelJson)
    return result