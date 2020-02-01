import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'database'))
import dbproduit as p
# import database as database
# from database import connexion as connexion
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
path = path+"/connectParameters.json"



def createProd(produitJson):
    try:
        result = p.createProduit(path,produitJson)
        return result
    except print(0):
        pass


def updateProd(produitJson,productId):
    result = p.updateProduit(path, produitJson,productId)
    return result

def deleteProd(productId):
    result = p.deleteProduit(path, productId)
    return result
def getAllProd():
    result = p.getAllProduit(path)
    return result
def getProdByCriteria(produitJson):
    try:
        result = p.getProduitByCriteria(path,produitJson)
        return result
    except print(0):
        pass
