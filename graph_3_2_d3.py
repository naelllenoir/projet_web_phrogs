# pip install pandas
# pip install d3blocks

# Import library
from d3blocks import D3Blocks

# Initialize
d3 = D3Blocks()


from collections import defaultdict
import pandas as pd

'''
scatter plot avec un point par annotation fonctionnelle
◦ en x : nombre de protéines dans des OGs ayant cette annotation
◦ en y : nombre d’OGs ayant cette annotation
◦ une couleur par grande catégorie fonctionnelle
'''

dicOG=defaultdict(list)
phrog=0
lenOG=0

with open ("MEGAclustout.mci.I20", "r") as cluster :
	for li in cluster :
		phrog+=1
		lenOG=len(li)
		dicOG['phrog'].append(phrog)
		dicOG['lenOG'].append(lenOG)
		
annot=pd.read_csv("phrog_annot.tsv", sep="\t")
annot=annot.fillna("undefined")

dfOG=pd.DataFrame(dicOG)

dftotal=annot.merge(dfOG, on='phrog')
xaxis=dftotal.groupby(['annot', 'category', 'color']).lenOG.sum()
yaxis=dftotal.groupby(['annot', 'category', 'color']).phrog.count()
final=pd.concat([xaxis, yaxis], axis=1).reset_index()

tooltip=final['category']

#print(xaxis, "\n", yaxis)
#print(dfOG)
#print(dftotal)

#chart = Scatterplot(dftotal, {x: xaxis, y: yaxis, title: dftotal[annot], xlabel: "Number of proteins in PhROGs with this annotation", ylabel: "Number of PhROGs with this annotation", halo: dftotal[color]})

chart = d3.scatter(final['lenOG'].values, final['phrog'].values, color=final['color'], xlim=[0, 25000], ylim=[0, 400], tooltip=tooltip, filepath='/home/naelllenoir/nalenoir/prograM1/test.html')



