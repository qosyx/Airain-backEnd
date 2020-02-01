import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'database'))
import dbtypeproduit as p
# import database as database
# from database import connexion as connexion
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
path = path+"/connectParameters.json"



def createtypeprod(typeproduitJson):
    result = p.createTypeProduit(path,typeproduitJson)
    return result

def updatetypeprod(typeproduitJson,typeproductId):
    result = p.updateTypeProduit(path, typeproduitJson,typeproductId)
    return result

def deletetypeprod(typeproductId):
    result = p.deleteTypeProduit(path, typeproductId)
    return result
def getAlltypeprod():
    result = p.getAllTypeProduit(path)
    return result
def gettypeprodByCriteria(typeproduitJson):
    result = p.getTypeProduitByCriteria(path,typeproduitJson)
    return result