# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 15:30:12 2024

@author: darvin
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Nom du fichier à importer
projet_chemin = 'enquete.xlsx'
df = pd.read_excel(projet_chemin)
# on organise les fichiers selon le account number fin de ne pas avoir de conflit dûe a une organisation diffférente entre 2 feuille de calcul
df = df.sort_values(by='Account number')

# on récupére toutes les feuilles sauf la 3 car elle est construites différemment
J = [1,3,4]
for i in J:
    df2 = pd.read_excel(projet_chemin,sheet_name = i)
    df2 = df2.sort_values(by='Account number')
    #on fusionne les colonnes en fonction de Account number
    df = pd.merge(df, df2, on='Account number', how='left')
    
# Supprimer les colonnes en double
df = df.loc[:, ~df.columns.duplicated()]
df = df.T.drop_duplicates().T
#on retire les "_x" ajouté par la fonction merge  
df.columns = df.columns.str.replace('_x$', '')
colonne = df.columns

#on verifie si on a pris le nécéssaire
colonne2 = pd.read_excel(projet_chemin).columns
for i in J:
    colonne3 = pd.read_excel(projet_chemin, sheet_name=i).columns
    colonne2 = colonne2.append(colonne3)

colonne2 = colonne2.drop_duplicates()

#chemin du 2ème fichiers
Stoxx_way = 'donnees_eco_ISIN.xlsx'

df_isin = pd.read_excel(Stoxx_way)
nom = df_isin.columns

#on recupére uniquement les ISIN
Isin = df_isin['ISIN Code']
#on se débarasse du 1er élément (NaN) car ce n'est pas un ISIN 
Isin = Isin.drop(0)
Isin = ' ' + Isin.astype(str)

#on filtre notre dateframe en conservant seulement ceux dont le ISIN est dans les ISIN du STOXX
df = df[df['ISINs'].isin(Isin)]

#on peut se débarasser de certaines colonnes inutiles ou manipuler les variables quali mais on ne le fera pas car il y a des alternatives

## Graphique
df['Response received date'] = pd.to_datetime(df['Response received date'])
df['Response received date'] = df['Response received date'].dt.date

# Créer un histogramme des dates
plt.figure(figsize=(10, 6))
plt.hist(df['Response received date'], bins=30, color='skyblue', edgecolor='black')

# Ajouter des étiquettes et un titre
plt.title('Histogramme des jours de réponse')
plt.xlabel('Dates')
plt.ylabel('Fréquence')

# Afficher l'histogramme
plt.show()

df['Country'].value_counts(normalize=True).loc[lambda x: x > 0.018].plot.pie(
    autopct='%1.1f%%',
    startangle=90, figsize=(8, 8), colors=plt.cm.Paired.colors
)

# Ajouter un titre
plt.title('Répartition par Pays')

# Afficher le diagramme en secteurs
plt.show()

total_entreprises = len(Isin)
entreprises_repondues = len(df)
entreprises_non_repondues = total_entreprises - entreprises_repondues

# Créer un graphique à barres empilées
plt.bar(['Répondues'], [entreprises_repondues], color='blue', label='Répondues')
plt.bar(['Répondues'], [entreprises_non_repondues], bottom=[entreprises_repondues], color='lightgray', label='Non répondues')

# Ajouter des étiquettes et un titre
plt.title('Réponses au Sondage')
plt.ylabel('Nombre d\'entreprises')
plt.legend()

# Afficher le graphique à barres empilées
plt.show()

secteur_counts = df['Industries'].value_counts(normalize=True)

# Filtrer les secteurs avec une proportion inférieure à 2%
secteurs_a_afficher = secteur_counts[secteur_counts >= 0.02]

# Créer un graphique à secteurs
plt.pie(secteurs_a_afficher, labels=secteurs_a_afficher.index, autopct='%1.1f%%', startangle=90, counterclock=False, colors=plt.cm.Paired.colors)

# Ajouter un titre
plt.title('Répartition par Secteur d\'activité')

# Afficher le graphique à secteurs
plt.show()

df['C1.1_Is there board-level oversight of climate-related issues within your organization?'] = df['C1.1_Is there board-level oversight of climate-related issues within your organization?'].replace({' Yes': 'Oui', ' No': 'Non'})

# Compter les occurrences des réponses
counts = df['C1.1_Is there board-level oversight of climate-related issues within your organization?'].value_counts()

# Créer un graphique à barres
plt.bar(counts.index, counts.values, color=['green', 'red'])

# Ajouter des étiquettes et un titre
plt.title('Entreprise ayant une surveillance au niveau du conseil dadministration par rapport au climat')
plt.xlabel('Réponse')
plt.ylabel('Entreprise')

# Afficher le graphique à barres
plt.show()

df['C1.3_Do you provide incentives for the management of climate-related issues, including the attainment of targets?'] = df['C1.3_Do you provide incentives for the management of climate-related issues, including the attainment of targets?'].replace({' Yes': 'Oui', ' No': 'Non'})

# Compter les occurrences des réponses
counts = df['C1.3_Do you provide incentives for the management of climate-related issues, including the attainment of targets?'].value_counts()

# Créer un graphique à barres
plt.bar(counts.index, counts.values, color=['green', 'red'])

# Ajouter des étiquettes et un titre
plt.title('Entreprise fournissant des incitations pour la gestion des problèmes liés au climat')
plt.xlabel('Réponse')
plt.ylabel('Entreprise')

# Afficher le graphique à barres
plt.show()

df['C0.5_Select the option that describes the reporting boundary for which climate-related impacts on your business are being reported. Note that this option should align with your consolidation approach to your Scope 1 and Scope 2 greenhouse gas inventory.']=df['C0.5_Select the option that describes the reporting boundary for which climate-related impacts on your business are being reported. Note that this option should align with your consolidation approach to your Scope 1 and Scope 2 greenhouse gas inventory.'].replace({' Operational control' : 'Contrôle opérationnel',' Financial control': 'Contrôle Financier','Hidden Answer': 'Réponse cachée'})
# Filtrer les réponses pour ne montrer que les catégories significatives (par exemple, celles avec une fréquence supérieure à un seuil)
seuil_frequence = 2 # Choisissez un seuil adapté à vos données
counts = df['C0.5_Select the option that describes the reporting boundary for which climate-related impacts on your business are being reported. Note that this option should align with your consolidation approach to your Scope 1 and Scope 2 greenhouse gas inventory.'].value_counts()
counts_filtre = counts[counts >= seuil_frequence]

# Créer un graphique à barres avec les catégories filtrées
plt.bar(counts_filtre.index, counts_filtre.values, color=['green', 'blue' , 'yellow' , 'grey'])

# Ajouter des étiquettes et un titre
plt.title('Répartition des réponses sur la limite de déclaration des impacts climatiques')
plt.xlabel('Réponse')
plt.ylabel('Nombre d\'entreprises')

plt.xticks(fontsize=7)
# Afficher le graphique à barres
plt.show()

df_non = df[df['C1.3_Do you provide incentives for the management of climate-related issues, including the attainment of targets?'] == 'Non']

# Créer un histogramme des dates
plt.figure(figsize=(10, 6))
plt.hist(df_non['Response received date'], bins=30, color='skyblue', edgecolor='black')

# Ajouter des étiquettes et un titre
plt.title('Histogramme des jours de réponse des entreprises ne fournissent pas d\'incitation à la gestion')
plt.xlabel('Dates')
plt.ylabel('Fréquence')

# Afficher l'histogramme
plt.show()

secteur_counts = df_non['Industries'].value_counts(normalize=True)

# Filtrer les secteurs avec une proportion inférieure à 2%
secteurs_a_afficher = secteur_counts[secteur_counts >= 0.02]

# Créer un graphique à secteurs
plt.pie(secteurs_a_afficher, labels=secteurs_a_afficher.index, autopct='%1.1f%%', startangle=90, counterclock=False, colors=plt.cm.Paired.colors)

# Ajouter un titre
plt.title('Diagramme camembert des seceteurs d\'activités où les entreprises ne fournissent pas d\'incitation à la gestion')

# Afficher le graphique à secteurs
plt.show()

df_non['Country'].value_counts(normalize=True).loc[lambda x: x > 0.018].plot.pie(
    autopct='%1.1f%%',
    startangle=90, figsize=(8, 8), colors=plt.cm.Paired.colors
)

# Ajouter un titre
plt.title('Diagramme camembert des pays où les entreprises ne fournissent pas d\'incitation à la gestion')

# Afficher le diagramme en secteurs
plt.show()

pays_count_non = df_non['Country'].value_counts()/ df['Country'].value_counts()
pays_count_non = pays_count_non.dropna()
pays_count_non = pays_count_non.drop('Malta')

fig, ax = plt.subplots()
#plt.bar(pays_count_non.index, pays_count_non)
bars = ax.bar(pays_count_non.index, pays_count_non)
ax.set_xticks(pays_count_non.index)
ax.set_xticklabels(pays_count_non.index, rotation=45, ha='right') 
# Ajoutez des étiquettes et un titre
plt.xlabel('nom des pays')
plt.ylabel('Proportion d\'entreprise par pays ne fournissant pas d\'incitation à la gestion de pb lié au climat')
plt.title('Diagramme à Bâtons')
plt.xticks(fontsize=8)
# Affichez le diagramme à bâtons
plt.show()
