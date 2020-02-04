import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0])))
import database.connexion as connexion
import json
import json



def createMagasin(parameters_path, jsonobject):

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
    strquery = "INSERT INTO magasin ( " + strkey + ") VALUES (" + strvalues + ")"
    db = connexion.connect(parameters_path)
    q = db.query(strquery)
    return q
def updateMagasin(parameters_path, jsonobject,magasinId):
    strquery = ""
    # jsonobject = json.loads(jsonobject)
    for key, value in jsonobject.items():
        strquery = strquery+ ", "+ key +"=" + "'"+value +"'" 
    strquery = strquery.strip(", ")
    strquery = "UPDATE magasin SET " + strquery + " WHERE magasinid = " +str(magasinId)
    print(strquery)
    db = connexion.connect(parameters_path)
    q = db.query(strquery)
    return q

def deleteMagasin(parameters_path, magasinId):
    strquery = "UPDATE magasin SET visible = False WHERE magasinid = " +str(magasinId)
    db = connexion.connect(parameters_path)
    q = db.query(strquery)
    return q

def getAllMagasin(parameters_path):
    result = []
    strquery =  "SELECT * from magasin Where visible =True "
    db = connexion.connect(parameters_path)
    for r in db.query(  # just for example
            strquery
            ).dictresult():
            result.append(r)
    return result

def getMagasinByCriteria(parameters_path,jsonobject):
    strquery = ""
    result = []
    # jsonobject = json.loads(jsonobject)
    for key, value in jsonobject.items():
        strquery = strquery+ " and "+ key +"=" + "'"+value +"'" 
    strquery = strquery.strip(" and ")
    strquery = "SELECT * From magasin WHERE " +strquery
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
    x = '{"typeMagasinid":"1"}'
 
    # x = '{"code":"arch","typeMagasinid":"1","libelle":"jean"}'
    getMagasinByCriteria(parameters_path,x)
    # updateProduit(parameters_path,x,2)
    # getAllProduit(parameters_path)
    # createProduit(parameters_path,x)