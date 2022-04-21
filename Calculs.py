# on importe les bibliothèques qui nous seront utiles
import statistics

from pandas import *  # pour lire, importer et manipuler des données sous forme tableur
from numpy import *  # pour faire des calculs
from matplotlib.pylab import *  # pour faire des graphiques
from scipy.stats import linregress

produit = read_excel('ClasseurBaseTicketsSAE.xlsx', 'Produit')
carteFidelite = read_excel('ClasseurBaseTicketsSAE.xlsx', 'CarteFidelite')
ville = read_excel('ClasseurBaseTicketsSAE.xlsx', 'Ville')
detailTicket = read_excel('ClasseurBaseTicketsSAE.xlsx', 'DetailTicket')

Unites_Stock = produit.Unites_Stock.values
print("En moyenne, il a", round(mean(Unites_Stock), 2), "unités en stock pour chaque produit.")

PrixUnit = produit.Prix_Unit.values
print("La variance des prix unitaires des produits est de", round(var(PrixUnit), 2))
print("L'écart type des prix unitaires des produits est de", round(std(PrixUnit), 2), "€.")

NbPerFoyer = carteFidelite.NbPerFoyer.values
print("La médiane du nombre de personnes par foyer est de :", np.percentile(NbPerFoyer, 50), "personne(s).")
print("Le premier quartile du nombre de personnes par foyer est de :", np.percentile(NbPerFoyer, 25), "personne(s).")
print("Le 10ème percentile du nombre de personnes par foyer est de :", np.percentile(NbPerFoyer, 10), "personne(s).")

Z = []
for i in PrixUnit:
    Z.append(round(i, 0))
plt.hist(Z, bins=[0, 5, 10, 15, 20, 60, 70], edgecolor='red')
title("Répartition des prix unitaires")
plt.show()

boxplot(NbPerFoyer)
gca().xaxis.set_ticklabels(['Tous les foyers'])
title("Variable NbPerFoyer")
show()

CodeRayon = produit.Code_rayon.values
boxplot([PrixUnit[CodeRayon == 32], PrixUnit[CodeRayon == 37], PrixUnit[CodeRayon == 54]])
gca().xaxis.set_ticklabels(['Légumes', 'Oeufs', 'Viandes'])
title("Variable Prix_Unit suivant le nom des rayons")
show()

distanceVille = ville.DistanceKM.values
Z = []
for i in distanceVille:
    Z.append(i)
plt.hist(Z, bins=[0, 10, 20, 30, 40, 50, 60, 70], edgecolor='red')
title("Répartition de la distance en km des villes par rapport au magasin")
plt.show()

nbPerFoyer = carteFidelite.NbPerFoyer.values
nbEnfant = carteFidelite.NbEnfant.values
cov = mean(nbPerFoyer*nbEnfant)-mean(nbPerFoyer)*mean(nbEnfant)
print("La covariance entre la variable du nombre de personnes par foyer et celle du nombre d'enfants par foyer est de", round(cov, 2))
nbPerFoyer = carteFidelite.NbPerFoyer.values
nbEnfant = carteFidelite.NbEnfant.values
params = linregress(nbPerFoyer, nbEnfant)
N = len(nbEnfant)
a = params[0]
b = params[1]
coefCor = params[2]
y_mod = []
for i in range(N):
    y_mod.append(a * nbPerFoyer[i] + b)
print("Le coefficient de corrélation entre le nombre d'enfants par rapport au nombre de personnes par foyer est de", round(coefCor), 2)
print("L'équation de la droite de régression est de : y =", round(a, 2),"x +", round(b, 2))
plot(nbPerFoyer, nbEnfant, "bo", label = "Point qui constitue le nuage de points")
plot(nbPerFoyer, y_mod, "r-", label = "Droite de régression")
xlabel("Nombre de personnes dans le foyer")
ylabel("Nombre d'enfants dans le foyer")
plot(mean(nbPerFoyer),mean(nbEnfant), marker="o", color="red", label = "Centre de gravité")
legend()
show()

prenom = carteFidelite.Prenom.values
print("Le prénom le plus représenté dans la liste des clients fidèles (mode) est", statistics.mode(prenom))



