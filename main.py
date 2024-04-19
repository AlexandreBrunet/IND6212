import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
    "Ouvert": 1
}

df['description_id'] = df['description'].map(description_id_mapping)
df['statut_id'] = df['statut'].map(statut_id_mapping)
df_filtered = df.dropna(subset=['description_id'])
nombre_de_lignes_2 = df_filtered.shape[0]
#Nombre de lignes dans le DataFrame : 6553
print("Nombre de lignes dans le DataFrame :", nombre_de_lignes_2)

counts_per_description_id = df_filtered['description_id'].value_counts().sort_index()
print(counts_per_description_id)

counts_per_statut_id = df_filtered['statut_id'].value_counts().sort_index()
print(counts_per_statut_id)

colonnes_selectionnees = df_filtered[['montant', 'description_id', 'statut_id']]
print(colonnes_selectionnees)



