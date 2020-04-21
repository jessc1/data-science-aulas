import pandas as pd
import matplotlib.pyplot as plt

nome_do_filme = "Totoro, o filme"
#print(nome_do_filme)
filmes = pd.read_csv("movies.csv")
filmes.columns = ["filmeId","titulo", "generos"]
filmes.head()
#print(filmes.head())
generos = pd.DataFrame(filmes["generos"].str.split("|").tolist(), index=filmes["filmeId"]).stack()

avaliacoes = pd.read_csv("ratings.csv")
#print(avaliacoes.head())
#print(len(avaliacoes))

avaliacoes.columns = ["usuarioId", "filmeId", "nota", "momento"]
#print(avaliacoes["nota"
avaliacoes_do_filme_1 = avaliacoes.query("filmeId==1")
#print(avaliacoes_do_filme_1.head())
#print(avaliacoes_do_filme_1.describe())
#print(avaliacoes_do_filme_1.mean())
#print(avaliacoes.describe())
#print(avaliacoes["nota"].mean())
#print(avaliacoes_do_filme_1["nota"].mean())
notas_medias_por_filme = avaliacoes.groupby("filmeId")["nota"].mean()
#print(notas_medias_por_filme.head())
filmes_com_media = filmes.join(notas_medias_por_filme, on="filmeId")
#print(filmes)                                     
filmes_com_media = filmes.join(notas_medias_por_filme, on="filmeId")
#print(nota_media.head())
#print(nota_media.sort_values("nota",ascending = True).head(20))
#print(avaliacoes.query("filmeId == 1")["nota"].plot())
#avaliacoes.query("filmeId == 1")["nota"].plot(kind='hist')
#plt.title("Avaliacões do filme toy story")
#plt.show()

# Desafio 1

#18 filmes sem avaliações?
filmes_sem_nota = filmes.merge(notas_medias_por_filme, how = 'left', on = 'filmeId')
filmes_sem_nota = filmes_sem_nota[pd.isnull(filmes_sem_nota['nota'])]
#print(filmes_sem_nota)

#DESAFIO 2
filmes_com_media = filmes_com_media.rename(columns ={'nota': 'nota_média'})
#print(filmes_com_media.columns)

#Desafio 3
filmes_com_qtd_votos = filmes.join(avaliacoes.groupby("filmeId")["nota"].count(), on = "filmeId")
filmes_com_qtd_votos = filmes_com_qtd_votos.rename(columns={"nota": "votos"})
#print(filmes_com_qtd_votos.sort_values(by="votos", ascending=False))

#Desafio 4

filmes_com_media["nota_média"] = filmes_com_media["nota_média"].round(2)
#print(filmes_com_media)

#Desafio 5
generos = pd.DataFrame(filmes["generos"].str.split("|").tolist(), index=filmes["filmeId"]).stack()
#print(generos.unique())

#Desafio 6
#print(generos.value_counts())

#Desafio 7
generos.value_counts().plot(kind="bar")
plt.show()




