# on importe les bibliothèques qui nous seront utiles
from pandas import *  # pour lire, importer et manipuler des données sous forme tableur
from numpy import *  # pour faire des calculs
from matplotlib.pylab import * # pour faire des graphiques

df = read_excel('ClasseurBaseTicketsSAE.xlsx')

Code_Rayon = df['Code_Rayon'].values
print(shape(Code_Rayon))