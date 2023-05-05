#!/usr/bin/python
'''
D3_partie_3_2_naell_lenoir.py
Auteur : Naell Lenoir
Ce programme permet de récupérer les données nécessaires à la réalisation d'un scatter plot :
scatter plot avec un point par annotation fonctionnelle
◦ en x : nombre de protéines dans des OGs ayant cette annotation
◦ en y : nombre d’OGs ayant cette annotation
◦ une couleur par grande catégorie fonctionnelle

Ce programme a été lancé pour créé le fichier csv présent dans le répertoire GitHub https://github.com/naelllenoir/projet_web_phrogs.
Il n'est donc pas nécessaire de le relancer pour afficher le scatter plot avec le script graph_d3_3_2_naell_lenoir_final.html,
car le fichier a été importé dans le répertoire GitHub.
Il suffit de lancer le fichier html pour faire apparaître le graphe.
'''

# pip install pandas

from collections import defaultdict
import pandas as pd


### Initialisation ###

dicOG=defaultdict(list)
phrog=0
lenOG=0


### Création du dictionnaire contenant le nombre de protéines par OG et le numéro d'OG ###

with open ("MEGAclustout.mci.I20", "r") as cluster :
	for li in cluster :
		li=li.rstrip().split()
		phrog+=1
		lenOG=len(li)
		dicOG['phrog'].append(phrog)
		dicOG['lenOG'].append(lenOG)


### Appel du fichier d'annotations tsv ###

annot=pd.read_csv("phrog_annot.tsv", sep="\t")
annot=annot.fillna("undefined")


### Création d'un dataframe avec les données du dictionnaire ###

dfOG=pd.DataFrame(dicOG)


### Association du dataframe avec le fichier d'annotation ###

dftotal=annot.merge(dfOG, on='phrog')


### Mise en forme des données finales ###

som_prot=dftotal.groupby(['annot', 'category', 'color']).lenOG.sum()
som_phrog=dftotal.groupby(['annot', 'category', 'color']).phrog.count()
final=pd.concat([som_prot, som_phrog], axis=1).reset_index()


### Partie facultative permettant de retirer les annotations trop peu nombreuses ###
final['annotation']=final['annot']
final.loc[(final['lenOG'] < 3000) & (final['phrog'] < 50), 'annotation'] = '  '


### Création du fichier csv ###
final.to_csv("data_d3_3_2_naell_lenoir.csv", sep=("\t"))
