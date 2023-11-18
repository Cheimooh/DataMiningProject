import pandas as pd

# Juste un .py qui fait pareil que le notebook mais que je trouve plus lisible

class PlayStoreData:
  def __init__(self):
    # TODO: ajouter un attribut pour les dico pour y acceder depuis d'autres fichiers
    self.df = pd.read_csv("data/googleplaystore.csv")

  ### Fonction de conversion des colonnes en numérique
  def col_to_num(self, col):
    self.df[col] = pd.to_numeric(self.df[col], errors="coerce")

  # TODO: Rajouter un commentaire plus descriptif
  ### Enum
  def dict_from_cat(self, col):
    return {valeur_unique: indice for indice, valeur_unique in enumerate(self.df[col].unique())}

  def dict_to_float(self, col, dictionary):
    self.df[col] = self.df[col].map(dictionary)
    self.col_to_num(col)


  #### Category
  def process_category(self):
    # Category, pourrait être convertie en données numériques, par ex 1 pour ART_AND_DESIGN, 2 pour FAMILLY etc
    dict_category = self.dict_from_cat("Category")
    self.dict_to_float("Category", dict_category)


  #### Reviews
  def process_reviews(self):
    # Reviews correspond au nombre de reviews, il faut donc le convertir en valeur numérique
    self.col_to_num("Reviews")


  #### Size
  def process_size(self):
    # Dans le cas présent, Size est un objet qui pourrait être convertis en une valeur numérique
    # Supprime les lignes où les valeurs sont pas interprétables (1,000+ et Varies with device)
    self.df = self.df.drop(self.df[self.df["Size"].str.contains('\+', regex=True)].index)
    self.df = self.df.drop(self.df[self.df["Size"].str.contains('Varies', regex=True)].index)

    self.df["Size"] = self.df["Size"].str.replace('M','000000')
    self.df["Size"] = self.df["Size"].str.replace('k', '000')

    self.df['Size'] = self.df['Size'].apply(lambda x: x[:-1] if '.' in x else x)
    self.df["Size"] = self.df["Size"].str.replace('.', '')

    self.col_to_num("Size")


  #### Installs
  def process_installs(self):
    # Correspond au nombre d'installations (ordre de grandeur) Il suffit d'enlever le +
    self.df["Installs"] = self.df["Installs"].str.replace('+', '')
    self.df["Installs"] = self.df["Installs"].str.replace(',', '')

    self.col_to_num("Installs")


  #### Type
  def process_type(self):
    # Semble correspondre au type de l'aplication (payante ou non). Peut etre convertie en valeur booleenne permettant de determiner si une app est payante ou non
    # La colonne "Prix" nous donne déjà l'infomation si le produit est gratuit ou non.
    self.df = self.df.drop(columns=["Type"])


  #### Price
  def process_price(self):
    # TODO: visiblement une donnée à enlever qui n'a pas été fait
    # Valeur numérique, il faut enlever le $ + (c'est quoi la donnée everyone ???)
    self.df["Price"] = self.df["Price"].str.replace('$', '')
    self.col_to_num("Price")


  #### Content Rating
  def process_content_rating(self):
    # on peut transformer tout ca en une valeur numérique
    dict_content_rating = self.dict_from_cat("Content Rating")
    self.dict_to_float("Content Rating", dict_content_rating)


  #### Genres
  def process_genres(self):
    # Probleme, cette colonne contient plusieurs infos, on va donc la split en 2 colonnes avant de la passée en valeurs numériques
    self.df[["Genres", "Genre Secondaire"]] = self.df["Genres"].str.split(";", expand=True)
    self.df = self.df.rename(columns={"Genres" : "Genre Principal"})

    ##### Genre Principal
    dict_genre_principal = self.dict_from_cat("GenrePrincipal")
    self.dict_to_float("Genre Principal", dict_genre_principal)

    ##### Genre Secondaire
    dict_genre_secondaire = self.dict_from_cat("GenreSecondaire")
    self.dict_to_float("Genre Secondaire", dict_genre_secondaire)


  #### Last Updated
  def process_last_updated(self):
    # TODO: Rajouter un commentaire ici
    # TODO: une ligne à enlever ou ça fait un truc ?
    #self.df['Last Updated'] = self.df['Last Updated'].str.replace(' [0-9]+,', '', regex=True)
    # TODO: presque sur que NaN se met pas en string comme ça
    self.df["Last Updated"] = self.df["Last Updated"].replace('1.0.19', "NaN")
    self.df["Last Updated"] = pd.to_datetime(self.df['Last Updated'], format='%B %d, %Y').dt.date


  #### Current Ver
  def process_current_ver(self):
    # Un peu inutile, dépend des applications.
    self.df = self.df.drop(columns=["Current Ver"])


  #### Android Ver
  def process_android_ver(self):
    # Similaire à Last Updated
    self.df = self.df.drop(columns=["Android Ver"])

  # Appelé depuis le main ou depuis un notebook par exemple
  def process_all(self):
    # On ne change pas "App", vu que c'est le nom des applications
    self.process_category()
    # On ne change pas "Rating", c'est déjà un float
    self.process_reviews()
    self.process_size()
    self.process_installs()
    self.process_type()
    self.process_price()
    self.process_content_rating()
    self.process_genres()
    self.process_last_updated()
    self.process_current_ver()
    self.process_android_ver()

    #### Dropna et export en csv
    self.df = self.df.dropna()
    self.df.to_csv("data/clean_dataset_googleplaystore.csv", index=False)


if __name__ == '__main__':
  test = PlayStoreData()
  test.process_all()