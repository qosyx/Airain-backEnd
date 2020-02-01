import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0])))
import database.connexion as connexion
import json
import json



def createProduit(parameters_path, jsonobject):

    strkey = ""
    strvalues = ""
    # jsonobject = json.loads(jsonobject)
    for key, value in jsonobject.items():
        strkey = strkey+ ", "+ key 
        strvalues = strvalues + ", "+ "'"+value + "'" 
    strkey = strkey.strip(", ")
    strkey = strkey + ", visible"
    strvalues = strvalues.strip(", ")
    strvalues = strvalues + ", True"
    strquery = "INSERT INTO produit ( " + strkey + ") VALUES (" + strvalues + ")"
    db = connexion.connect(parameters_path)
    q = db.query(strquery)
    return q
def updateProduit(parameters_path, jsonobject,produitid):
    strquery = ""
    # jsonobject = json.loads(jsonobject)
    for key, value in jsonobject.items():
        strquery = strquery+ ", "+ key +"=" + "'"+value +"'" 
    strquery = strquery.strip(", ")
    strquery = "UPDATE produit SET " + strquery + " WHERE produitid = " +str(produitid)
    print(strquery)
    db = connexion.connect(parameters_path)
    q = db.query(strquery)
    return q

def deleteProduit(parameters_path, produitid):
    strquery = "UPDATE produit SET visible = False WHERE produitid = " +str(produitid)
    db = connexion.connect(parameters_path)
    q = db.query(strquery)
    return q

def getAllProduit(parameters_path):
    result = []
    strquery =  "SELECT * from produit Where visible =True "
    db = connexion.connect(parameters_path)
    for r in db.query(  # just for example
            strquery
            ).dictresult():
            result.append(r)
    return result

def getProduitByCriteria(parameters_path,jsonobject):
    strquery = ""
    result = []
    # jsonobject = json.loads(jsonobject)
    for key, value in jsonobject.items():
        strquery = strquery+ " and "+ key +"=" + "'"+value +"'" 
    strquery = strquery.strip(" and ")
    strquery = "SELECT * From produit WHERE " +strquery
    db = connexion.connect(parameters_path)
    # q = db.query(strquery)
    # result = q.getresult()
    for r in db.query(  # just for example
            strquery
            ).dictresult():
            result.append(r)
    return result

if __name__ == "__main__":
    parameters_path = sys.argv[1]
    # replace x by dict
    x = '{"typeproduitid":"1"}'
 
    # x = '{"code":"arch","typeproduitid":"1","libelle":"jean"}'
    getProduitByCriteria(parameters_path,x)
    # updateProduit(parameters_path,x,2)
    # getAllProduit(parameters_path)
    # createProduit(parameters_path,x)