Sonia DAKHLI, Nino RAVELLA, Maeva SOMNY
# DataMiningProject
## Sujet : Applications du Google PlayStore

### Architecture
- **/** : les fichiers source de l'analyse :
  - *pretraitement.ipynb* : Partie III. Pré-traitement du dataset.
  - *clustering.ipynb* : Partie IV.A. Clustering.
  - *frequent_patterns.ipynb* : Partie IV.B. Frequent Patterns.
  - *keywords.ipynb*: Partie IV.C. Analyse des mots clés dans les titres.
- **/data/** : contient les datasets :
  - *googleplaystore.csv* : dataset utilisé.
  - *clean_dataset_googleplaystore* : dataset après pré-traitement.
  - *clean_dataset_googleplaystore_cat_str* : dataset après pré-traitement avec les noms de catégorie et de genre gardés en String.
  - *apriori.csv* : dataframe utilisé pour applique l'algorithme Apriori.
- **/output/** : contient les sorties des frequent patterns (Partie IV.B.).

### Données
Données du PlayStore collectées en 2018. Les informations contenues dans ce dataset sont : 
- **App** : nom de l'application.
- **Category** : catégorie (ART_AND_DESIGN, AUTO_AND_VEHICLES,...).
- **Rating** : score de l'application (entre 0 et 5).
- **Reviews** : nombre d'avis.
- **Size** : taille de l'application.
- **Installs** : nombre d'installations.
- **Type** : gratuit ou payant.
- **Price** : prix de l'application.
- **Content Rating** : public.
- **Genres** : couple Genre Principal, Genre Secondaire.
- **Last Updated** : dernière mise à jour.
- **Current Ver** : version actuelle.
- **Android Ver** : version Android compatible.
