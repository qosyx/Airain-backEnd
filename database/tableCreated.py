import sys
import os
import connexion as connexion
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
path=path+"/connectParameters.json"

 
def createTable(db):
     #typeproduit
    db.query("create table if not exists typeproduit "
    "(typeproduitid serial primary key, code varchar, libelle varchar, "
    "visible boolean"
    ")"
    )
    db.query("create table if not exists produit "
    "(produitid serial primary key, code varchar, libelle varchar, "
    "typeproduitid INTEGER REFERENCES typeproduit(typeproduitid),"
    "visible boolean"
    ")"
    )
    db.query("create table if not exists magasin "
    "(magasinid serial primary key, code varchar, libelle varchar, "
    "visible boolean"
    ")"
    )
    db.query("create table if not exists client "
    "(clientid serial primary key, nom varchar, prenom varchar, "
    "visible boolean"
    ")"
    )
    db.query("create table if not exists typepersonnel "
    "(typepersonnelid serial primary key, code varchar, libelle varchar,"
    "visible boolean"
    ")"
    )
    db.query("create table if not exists personnel "
    "(personnelid serial primary key, code varchar, nom varchar,"
    "prenom varchar, statut varchar, typepersonnelid INTEGER REFERENCES typepersonnel(typepersonnelid), "
    "visible boolean"
    ")"
    )
    db.query("create table if not exists acquisition "
    "(acquisitionid serial primary key, code varchar, libelle varchar,"
    "quantite varchar, dateacquisition date, "
    "magasinid INTEGER REFERENCES magasin(magasinid),"
    "personnelid INTEGER REFERENCES personnel(personnelid),"
    "produitid INTEGER REFERENCES produit(produitid),"
    "visible boolean"
    ")"
    )
    db.query("create table if not exists officine "
    "(officineid serial primary key,codeproduit varchar, code varchar, libelle varchar,"
    "quantite varchar, dateaofficine date,prixvente varchar,"
    "receveurid INTEGER REFERENCES personnel(personnelid),"
    "transmetteurid INTEGER REFERENCES personnel(personnelid),"
    "visible boolean"
    ")"
    )
    db.query("create table if not exists achat "
    "(achatid serial primary key,codeproduit varchar, codeachat varchar,"
    "quantite varchar, dateaachat date,prixventeunitaire varchar, prixventeligne varchar,"
    "clientid INTEGER REFERENCES client(clientid),"
    "officineid INTEGER REFERENCES officine(officineid),"
    "visible boolean"
    ")"
    )
    db.query("create table if not exists typeetat "
    "(typeetatid serial primary key, code varchar, libelle varchar, "
    "visible boolean"
    ")"
    )
    db.query("create table if not exists etatachat "
    "(etatachatid serial primary key, code varchar, dateetatachat date, "
    "typeetatid INTEGER REFERENCES typeetat(typeetatid),"
    "achatid INTEGER REFERENCES achat(achatid),"
    "visible boolean"
    ")"
    )

    db.query("create table if not exists commande "
    "(commandeid serial primary key, codecommande varchar, codeproduit varchar, libelle varchar, datecommande date, "
    "quantitedemande varchar, quantiteaccorde varchar,"
    "acquisitionid INTEGER REFERENCES acquisition(acquisitionid),"
    "personneldemandeid INTEGER REFERENCES personnel(personnelid),"
    "visible boolean"
    ")"
    )
    db.query("create table if not exists etatcommande "
    "(etatcommandeid serial primary key, codeetat varchar, libelle varchar, dateetatcommande date, "
    "codeproduit varchar, libelleproduit varchar, quantitedemande varchar, quantiteaccorde varchar,"
    "commandeid INTEGER REFERENCES commande(commandeid),"
    "personnelaccordid INTEGER REFERENCES personnel(personnelid),"
    "visible boolean"
    ")"
    )

def execution(parameters_path):
    r=connexion.connect(parameters_path)
    createTable(r)

# def dropTableByName(db,tablename):
#     myquery="drop table "+tablename
#     db.query(myquery)
if __name__ == '__main__':
    print(path)
    # # Charger tous les paramètres
    parameters_path = sys.argv[1]
    r=connexion.connect(parameters_path)
    createTable(r)
    # dropTableByName(r,"fruits")