# on importe les bibliothèques qui nous seront utiles
from pandas import *  # pour lire, importer et manipuler des données sous forme tableur
from numpy import *  # pour faire des calculs
from matplotlib.pylab import *  # pour faire des graphiques

produit = read_excel('ClasseurBaseTicketsSAE.xlsx', 'Produit')
carteFidelite = read_excel('ClasseurBaseTicketsSAE.xlsx', 'CarteFidelite')

Unites_Stock = produit.Unites_Stock.values
print("En moyenne, il a", round(mean(Unites_Stock), 2), "unités en stock pour chaque produit.")

PrixUnit = produit.Prix_Unit.values
print("La variance des prix unitaires des produits est de", round(var(PrixUnit), 2))
print("L'écart type des prix unitaires des produits est de", round(std(PrixUnit), 2), "€.")

NbPerFoyer = carteFidelite.NbPerFoyer.values
print("La médiane du nombre de personnes par foyer est de :", np.percentile(NbPerFoyer, 50), "personnes.")
print("Le premier quartile du nombre de personnes par foyer est de :", np.percentile(NbPerFoyer, 25), "personnes.")
print("Le 10ème percentile du nombre de personnes par foyer est de :", np.percentile(NbPerFoyer, 10), "personnes.")

Z = []
for i in PrixUnit:
    Z.append(round(i, 0))
plt.hist(Z, range=(0, 70), bins=[0, 5, 10, 15, 20, 60, 70], edgecolor='red')
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
