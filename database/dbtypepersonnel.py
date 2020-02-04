import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0])))
import database.connexion as connexion
import json
import json

def createTypepersonnel(parameters_path, jsonobject):
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
    strquery = "INSERT INTO typepersonnel ( " + strkey + ") VALUES (" + strvalues + ")"
    # print(strquery)
    db = connexion.connect(parameters_path)
    q = db.query(strquery)
    print(q)
    return q

def updateTypepersonnel(parameters_path, jsonobject,typepersonnelid):
    strquery = ""
    # jsonobject = json.loads(jsonobject)
    for key, value in jsonobject.items():
        strquery = strquery+ ", "+ key +"=" + "'"+value +"'" 
    strquery = strquery.strip(", ")
    strquery = "UPDATE typepersonnel SET " + strquery + " WHERE typepersonnelid = " +str(typepersonnelid)
    db = connexion.connect(parameters_path)
    q = db.query(strquery)
    return q

def deleteTypepersonnel(parameters_path, typepersonnelid):
    strquery = "UPDATE typepersonnel SET visible = False WHERE typepersonnelid = " +str(typepersonnelid)
    db = connexion.connect(parameters_path)
    q = db.query(strquery)
    return q

def getAllTypepersonnel(parameters_path):
    result = []
    strquery =  "SELECT DISTINCT * from typepersonnel Where visible =True "
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
def getTypepersonnelByCriteria(parameters_path,jsonobject):
    strquery = ""
    result = []
    # jsonobject = json.loads(jsonobject)
    for key, value in jsonobject.items():
        strquery = strquery+ " and "+ key +"=" + "'"+value +"'" 
    strquery = strquery.strip(" and ")
    strquery = "SELECT DISTINCT * From typepersonnel WHERE " +strquery
    db = connexion.connect(parameters_path)
    # q = db.query(strquery)
    # result = q.getresult()
    for r in db.query(  # just for example
            strquery
            ).dictresult():
            result.append(r)
    return result

if __name__ == "__main__":
    pass