import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'database'))
import dbacquisition as p
# import database as database
# from database import connexion as connexion
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
path = path+"/connectParameters.json"



def createAcquisition(acquisitionJson):
    result = p.createAcquisition(path,acquisitionJson)
    return result


def updateAcquisition(acquisitionJson,acquisitionId):
    result = p.updateAcquisition(path, acquisitionJson,acquisitionId)
    return result

def deleteAcquisition(acquisitionId):
    result = p.deleteAcquisition(path, acquisitionId)
    return result

def getAllAcquisition():
    result = p.getAllAcquisition(path)
    return result

def getAcquisitionByCriteria(acquisitionJson):
    result = p.getAcquisitionByCriteria(path,acquisitionJson)
    return result
