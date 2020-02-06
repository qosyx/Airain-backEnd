import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'database'))
import dbpersonnel as p
# import database as database
# from database import connexion as connexion
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
path = path+"/connectParameters.json"



def createPersonnel(personnelJson):
    result = p.createPersonnel(path,personnelJson)
    return result


def updatePersonnel(personnelJson,personnelId):
    result = p.updatePersonnel(path, personnelJson,personnelId)
    return result

def deletePersonnel(personnelId):
    result = p.deletePersonnel(path, personnelId)
    return result
def getAllPersonnel():
    result = p.getAllPersonnel(path)
    return result
def getPersonnelByCriteria(personnelJson):
    result = p.getPersonnelByCriteria(path,personnelJson)
    return result
