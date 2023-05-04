#pip install plotly
#pip install pandas

from collections import defaultdict
import re
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

genomes=pd.read_csv("info_genomes.tsv", sep="\t", index_col="Locus")

virus_host_fam=defaultdict(lambda:defaultdict(int))
viral_fam=[]
host_class=[]
nombre=[]
dorderhost=defaultdict(list)

with open("info_genomes.tsv", "r") as infos :
	for li in infos :
		li=li.rstrip().split("\t")
		search_fam=re.search("\w+viridae", li[5], re.I)
		if search_fam != None :
			fam=search_fam.group()
		elif search_fam == None and li[5] != "Taxonomy":
			fam="other"
		if li[11] != "class" :
			host=li[11]
			virus_host_fam[fam][host]+=1
			if li[12] not in dorderhost[host] :
				dorderhost[host].append(li[12])

print(dorderhost)					

for fam in virus_host_fam :
	for host in virus_host_fam[fam] :
		viral_fam.append(fam)
		host_class.append(host)
		nombre.append(virus_host_fam[fam][host])



df=pd.DataFrame({'Host':list(host_class), 'Virus':list(viral_fam), 'Nb':list(nombre)})

print(df)

size=df['Nb']
fig=go.Figure(data=[go.Scatter(x=df['Host'], y=df['Virus'], text=df['Nb'], mode='markers', marker=dict(size=size, sizemode='area', sizeref=max(size)/(30.**2), sizemin=2))])


fig.update_layout(title=dict(text='Bubble plot du nombre de virus de familles virales infectant leurs hôtes', font=dict(size=20)), title_x=0.5, title_y=0.95,
	xaxis=dict(
		title='host domain and class',
		gridcolor='white',
		gridwidth=2,
	),
	yaxis=dict(
		title='virus taxonomy',
		gridcolor='white',
		gridwidth=2
	),
	paper_bgcolor='rgb(254, 254, 254)',
	plot_bgcolor='rgb(243, 243, 243)',
)

fig.show()

