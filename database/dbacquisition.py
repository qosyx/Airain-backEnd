import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0])))
import database.connexion as connexion
import json
import json



def createAcquisition(parameters_path, jsonobject):

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
    strquery = "INSERT INTO acquisition ( " + strkey + ") VALUES (" + strvalues + ")"
    db = connexion.connect(parameters_path)
    q = db.query(strquery)
    return q
    
def updateAcquisition(parameters_path, jsonobject,AcquisitionId):
    strquery = ""
    # jsonobject = json.loads(jsonobject)
    for key, value in jsonobject.items():
        strquery = strquery+ ", "+ key +"=" + "'"+value +"'" 
    strquery = strquery.strip(", ")
    strquery = "UPDATE acquisition SET " + strquery + " WHERE acquisitionid = " +str(AcquisitionId)
    print(strquery)
    db = connexion.connect(parameters_path)
    q = db.query(strquery)
    return q

def deleteAcquisition(parameters_path, AcquisitionId):
    strquery = "UPDATE acquisition SET visible = False WHERE acquisitionid = " +str(AcquisitionId)
    db = connexion.connect(parameters_path)
    q = db.query(strquery)
    return q

def getAllAcquisition(parameters_path):
    result = []
    strquery =  "SELECT * from acquisition Where visible =True "
    db = connexion.connect(parameters_path)
    for r in db.query(  # just for example
            strquery
            ).dictresult():
            result.append(r)
    return result

def getAcquisitionByCriteria(parameters_path,jsonobject):
    strquery = ""
    result = []
    # jsonobject = json.loads(jsonobject)
    for key, value in jsonobject.items():
        strquery = strquery+ " and "+ key +"=" + "'"+value +"'" 
    strquery = strquery.strip(" and ")
    strquery = "SELECT * From acquisition WHERE " +strquery
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