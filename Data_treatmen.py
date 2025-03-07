import pandas as pd 
import numpy  as np 

feature_data = pd.read_csv("dataset_1.csv", index_col=0)
'''print(feature_data)
print(feature_data.describe())
con el describe() nos da la info del documento que estamos usando la info como una media, min y max
print(feature_data.info()) 
con el info() no da la informacion de el numero de columnas, sus nombres, que tipo de datos se usan 
'''
#CONJUNTO DE COLUMNAS CATEGORICAS

set_gender = set(feature_data["Género"].to_list())
set_education = set(feature_data["Nivel_Educación"].to_list())
set_city = set(feature_data["Ciudad"].to_list())

print(set_gender)
print(set_education)
print(set_city)


#TRATAMIENTO DE DATOS, ORGANIZAR LOS DATOS

#VALORES NEGATIVOS
feature_data["Edad"] = feature_data["Edad"].apply(lambda x: np.nan if x < 0 else x)
feature_data["Ingresos"] = feature_data["Ingresos"].apply(lambda x: np.nan if x < 0 else x)
feature_data["Hijos"] = feature_data["Hijos"].apply(lambda x: np.nan if x < 0 else x)

# PONER O IMPUTAR VALORES FALTANTES 
for column in ["Edad","Ingresos","Hijos"]:
    mediana_value = feature_data[column].median() #usasmos el metodo median que es trabajar con la mediana 
    feature_data[column].fillna(mediana_value, inplace=True)

for column in ["Género", "Ciudad"]:
    moda_values = feature_data[column].mode()[0]
    feature_data.fillna({column: moda_values}, inplace=True)


#ESTANDARIZACION O MAPEO DE LOS DATOS 
map_education = {
    "Bachelors" : "Bachelor",
    "mastre": "Master",
    "pHd": "PhD",
    "no education": "NE"
}
feature_data["Nivel_Educación"].replace(map_education, inplace=True)
feature_data["Nivel_Educación"].fillna("NE", inplace=True)

#CASTEO DE TIPOS QUE CADA COLUMNA SI TENGA SU TIPO DE DATO CORRECTO
feature_data["Edad"] = feature_data["Edad"].astype(int)
feature_data["Hijos"] = feature_data["Hijos"].astype(int)
feature_data["Ingresos"] = feature_data["Ingresos"].astype(float)
feature_data["Altura"] = feature_data["Altura"].astype(float)

print(feature_data)
print(feature_data.describe())
print(feature_data.info())
