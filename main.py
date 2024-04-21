import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


df = pd.read_csv('./data/violations.csv')
nombre_de_lignes = df.shape[0]
#Nombre de lignes dans le DataFrame : 7106
print("Nombre de lignes dans le DataFrame :", nombre_de_lignes)
num_categories = df['description'].nunique()
#Nombre de categorie distinct pour la description de l'infraction: 60
print("Nombre de categorie distinct pour la description de l'infraction:", num_categories)

#Créer un dictionnaire associant chaque description à son identifiant : 10 categories les plus populaire avec echantillon > 60 lignes
description_id_mapping = {
    "Les lieux, véhicules, équipements, matériaux et ustensiles servant à la préparation au conditionnement, à l'entreposage, au transport, à l'étiquetage et au service des produits, ainsi que les autres installations et locaux sanitaires, doivent être propres.": 1,
    "Le produit altérable à la chaleur à l'exception des fruits et légumes frais entiers doit être refroidi sans retard et maintenu constamment à une température interne et ambiante ne dépassant pas 4C jusqu'à sa livraison au consommateur, sauf pendant le temps requis pour l'application d'un procédé de fabrication ou d'un traitement reconnu en industrie alimentaire et qui exige une plus haute température.": 2,
    "Le lieu ou le véhicule doit être exempt de contaminants, de polluants, de toute espèce d'animaux y compris les insectes et les rongeurs ou de leurs excréments.": 3,
    "Le produit périssable vendu chaud ou servi chaud au consommateur doit être gardé à une température interne d'au moins 60C jusqu'à sa livraison.": 4,
    "Les personnes affectées à la préparation des produits, au lavage ou au nettoyage du matériel et de l'équipement doivent: porter un bonnet ou une résille propre qui recouvre entièrement les cheveux; porter un couvre-barbe propre qui recouvre entièrement la barbe.": 5,
    "Tout produit conditionné en vue de la vente doit porter, en caractères indélébiles, très lisibles et apparents, sur le récipient, l'emballage ou l'enveloppe qui le contient les inscriptions nécessaires pour révéler la nature, l'état, la composition, l'utilisation, la quantité exacte, l'origine et toute particularité du produit; les nom et adresse du fabricant, préparateur, conditionneur, emballeur, fournisseur ou distributeur; le lieu de fabrication, préparation ou conditionnement du produit. L'énumération des composants doit figurer par ordre d'importance décroissant. L'indication de poids doit tenir compte de la perte que peut normalement subir le produit après son conditionnement et être exprimée en poids net.": 6,
    "Nul ne peut, sans être titulaire d'un permis en vigueur, exploiter un lieu ou un véhicule où est exercée l'activité de restaurateur.": 7,
    "Est prohibée toute tromperie ou tentative de tromperie, toute déclaration ou indication fausse, inexacte ou trompeuse, sous quelque forme et par quelque moyen que ce soit: a) sur la nature, l'état, la composition, l'identité, la provenance, l'origine, l'utilisation, la destination, la qualité, la quantité, la valeur, le prix ou une particularité du produit; b) sur le lieu, la date ou les procédés de préparation, fabrication, conservation ou conditionnement du produit; c) sur le mode d'emploi ou de conservation du produit; d) sur l'identité, les qualités ou aptitudes du producteur, préparateur, fabricant, conserveur, conditionneur, distributeur ou de l'agent de vente ou de livraison du produit.": 8,
    "Nul ne peut préparer, détenir en vue de la vente ou de la fourniture de services moyennant rémunération, recevoir, acheter pour fins de revente, mettre en vente ou en dépôt, vendre, donner à des fins promotionnelles, transporter, faire transporter ou accepter pour transport, tout produit destiné à la consommation humaine qui est impropre à cette consommation, qui est altéré de manière à le rendre impropre à cette consommation, dont l'innocuité n'est pas assurée pour cette consommation ou qui n'est pas conforme aux exigences de la présente loi et des règlements.": 9,
    "Dans un local, une aire ou un véhicule utilisé pour la préparation des produits personne ne peut y faire usage de tabac.": 10
}

#Créer un dictionnaire associant chaque statut à son identifiant:
statut_id_mapping =  {
    "Fermé": 0,
    "Fermé changement d'exploitant": 0,
    "Ouvert": 1,
    "Sous inspection fédérale": 1
}

categorie_id_mapping =  {
    "Restaurant": 1,
    "Restaurant service rapide": 2,
    "Épicerie avec préparation": 3,
    "Boucherie-épicerie": 4,
    "Pâtisserie": 5,
    "Boulangerie": 6,
    "Casse-croûte": 7,
    "Restaurant mets pour emporter": 8,
    "Supermarché": 9,
    "Traiteur": 10,
    "Charcuterie/fromage": 11,
    "Charcuterie": 12,
    "Épicerie": 13,
    "Poissonnerie": 14,
    "Brasserie": 15
}

#adding description_id column
df['description_id'] = df['description'].map(description_id_mapping)
#adding statut_id column
df['statut_id'] = df['statut'].map(statut_id_mapping)
#adding categorie_id column
df['categorie_id'] = df['categorie'].map(categorie_id_mapping)

#remove columns without any description
df_filtered = df.dropna(subset=['description_id'])

#Nombre de categorie distint d'etablissement: 42
num_etablissement = df['categorie'].nunique()
print("Nombre de categorie distinct d'etablissement:", num_etablissement)

#Nombre de lignes dans le DataFrame : 6553
nombre_de_lignes_2 = df_filtered.shape[0]
print("Nombre de lignes dans le DataFrame avec les principales catégories:", nombre_de_lignes_2)

# Nombre de lignes avec statut_id = 0
nb_lignes_statut_0 = df_filtered[df_filtered['statut_id'] == 0].shape[0]
print("Nombre de lignes avec statut_id égal à 0 :", nb_lignes_statut_0)

# Nombre de lignes avec statut_id = 1
nb_lignes_statut_1 = df_filtered[df_filtered['statut_id'] == 1].shape[0]
print("Nombre de lignes avec statut_id égal à 1 :", nb_lignes_statut_1)

# Comptage du nombre de lignes par catégorie dans df_filtered
comptage_par_categorie = df_filtered['categorie'].value_counts()

# Filtrage des catégories avec un count >= 30
catégories_filtrees = comptage_par_categorie[comptage_par_categorie >= 30].index

# Filtrage des lignes dans df_filtered
df_filtre_final = df_filtered[df_filtered['categorie'].isin(catégories_filtrees)]

# Affichage du nombre de lignes dans le DataFrame filtré
nombre_de_lignes_final = df_filtre_final.shape[0]
print("Nombre de lignes dans le DataFrame filtré:", nombre_de_lignes_final)

num_etablissement_2 = df_filtre_final['categorie'].nunique()
print("Nombre de categorie distinct d'etablissement:", num_etablissement_2)

print(df_filtre_final.head(10))
