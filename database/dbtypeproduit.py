import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0])))
import database.connexion as connexion
import json
import json

def createTypeProduit(parameters_path, jsonobject):
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
    strquery = "INSERT INTO typeproduit ( " + strkey + ") VALUES (" + strvalues + ")"
    # print(strquery)
    db = connexion.connect(parameters_path)
    q = db.query(strquery)
    print(q)
    return q

def updateTypeProduit(parameters_path, jsonobject,typeproduitid):
    strquery = ""
    # jsonobject = json.loads(jsonobject)
    for key, value in jsonobject.items():
        strquery = strquery+ ", "+ key +"=" + "'"+value +"'" 
    strquery = strquery.strip(", ")
    strquery = "UPDATE typeproduit SET " + strquery + " WHERE typeproduitid = " +str(typeproduitid)
    db = connexion.connect(parameters_path)
    q = db.query(strquery)
    return q

def deleteTypeProduit(parameters_path, typeproduitid):
    strquery = "UPDATE typeproduit SET visible = False WHERE typeproduitid = " +str(typeproduitid)
    db = connexion.connect(parameters_path)
    q = db.query(strquery)
    return q

def getAllTypeProduit(parameters_path):
    result = []
    strquery =  "SELECT DISTINCT * from typeproduit Where visible =True "
    db = connexion.connect(parameters_path)
    # q = db.query(strquery)
    # result = q.getresult()
    # print(result)
    for r in db.query(  # just for example
            strquery
            ).dictresult():
            result.append(r)
    return result
# x = '{"code":"jonh","libelle":"jb","visible":"True"}'
def getTypeProduitByCriteria(parameters_path,jsonobject):
    strquery = ""
    result = []
    # jsonobject = json.loads(jsonobject)
    for key, value in jsonobject.items():
        strquery = strquery+ " and "+ key +"=" + "'"+value +"'" 
    strquery = strquery.strip(" and ")
    strquery = "SELECT DISTINCT * From typeproduit WHERE " +strquery
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
    x = '{"code":"jonh","libelle":"jb"}'
    getTypeProduitByCriteria(parameters_path,x)
    # updateTypeProduit(parameters_path,x,1)
    # getAllTypeProduit(parameters_path)
    # createTypeProduit(parameters_path,x)