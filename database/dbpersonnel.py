import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0])))
import database.connexion as connexion
import json
import json



def createPersonnel(parameters_path, jsonobject):

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
    strquery = "INSERT INTO personnel ( " + strkey + ") VALUES (" + strvalues + ")"
    db = connexion.connect(parameters_path)
    q = db.query(strquery)
    return q
def updatePersonnel(parameters_path, jsonobject,personnelid):
    strquery = ""
    # jsonobject = json.loads(jsonobject)
    for key, value in jsonobject.items():
        strquery = strquery+ ", "+ key +"=" + "'"+value +"'" 
    strquery = strquery.strip(", ")
    strquery = "UPDATE personnel SET " + strquery + " WHERE personnelid = " +str(personnelid)
    print(strquery)
    db = connexion.connect(parameters_path)
    q = db.query(strquery)
    return q

def deletePersonnel(parameters_path, personnelid):
    strquery = "UPDATE personnel SET visible = False WHERE personnelid = " +str(personnelid)
    db = connexion.connect(parameters_path)
    q = db.query(strquery)
    return q

def getAllPersonnel(parameters_path):
    result = []
    strquery =  "SELECT * from personnel Where visible =True "
    db = connexion.connect(parameters_path)
    for r in db.query(  # just for example
            strquery
            ).dictresult():
            result.append(r)
    return result

def getPersonnelByCriteria(parameters_path,jsonobject):
    strquery = ""
    result = []
    # jsonobject = json.loads(jsonobject)
    for key, value in jsonobject.items():
        strquery = strquery+ " and "+ key +"=" + "'"+value +"'" 
    strquery = strquery.strip(" and ")
    strquery = "SELECT * From personnel WHERE " +strquery
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