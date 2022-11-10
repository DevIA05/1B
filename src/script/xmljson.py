import xmltodict, json
from os import walk

def  getListeFichiers(dossier) :
    listeFichiers = []
    for (repertoire, sousRepertoires, fichiers) in walk(dossier):
        listeFichiers.extend(fichiers)
        break                            
    # print(listeFichiers)
    return listeFichiers

def traiterUnFichier(fichierQuizz):
    with open(fichierQuizz,'r') as myfile:
        obj = xmltodict.parse(myfile.read())
    return obj

# \..* 
# import re

monRepertoire = 'questionnaires/'
listeFichiers = getListeFichiers(monRepertoire)

for fich in range(0,len(listeFichiers)):
    json_data = json.dumps(traiterUnFichier(monRepertoire+listeFichiers[fich]))
    # print(json_data)
    # x = re.sub("\..*","" ,listeFichiers[fich])
    pathOutput = "qjson/"+listeFichiers[fich] +".json"
    with open(pathOutput, "w") as outfile:outfile.write(json_data)
