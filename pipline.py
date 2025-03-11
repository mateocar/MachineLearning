import pandas as pd 
import numpy as np


#CORRECCION DE DATOS EN LOS PIPLINES O LLAMADAS DE FUNCIONES EN CADENA 



# CREAR UNA FUNCION PARA REEMPLAZAR VALORES EN CUALQUIER COLUMNA 

def remove_negative_values(data_frame, column):
    data_frame[column] = data_frame[column].apply(lambda x: np.nan if x < 0 else x) 
    return data_frame

def remove_outliers(data_frame, column, threshold = 2):
    column_mean = data_frame[column].mean()
    column_standar= data_frame[column].std()

    data_frame[column] = data_frame[column].mask(((data_frame[column] - column_mean) / column_standar).abs() > threshold, column_mean)

    return data_frame

def map_colunn_values(data_frame, column, mapping_dict):
    data_frame[column] = data_frame[column].apply(lambda value:mapping_dict.get(value, value))
    
    return data_frame


def fill_in_column_with_na(data_frame, column, fill_value):
    data_frame[column].fillna(fill_value, inplace = True)

    return data_frame


def pre_data(data_frame):
    map_education = {
        "Bachelors" : "Bachelor",
        "mastre": "Master",
        "pHd": "PhD",
        "no education": "NE"
    }

    map_of_gender = {
        "m": "M",
        "f": "F"
    }

    return(
        data_frame.pipe(remove_negative_values, "Edad")
        .pipe(remove_negative_values, "Ingresos")
        .pipe(remove_negative_values, "Hijos")
        .pipe(remove_outliers, "Edad")
        .pipe(remove_outliers, "Ingresos")
        .pipe(remove_outliers, "Altura")
        .pipe(remove_outliers, "Hijos")
        .pipe(map_colunn_values, "Nivel_Educación", map_education)
        .pipe(map_colunn_values, "Género", map_of_gender)
        .pipe(fill_in_column_with_na, "Ciudad", "Desconocido")
        .pipe(fill_in_column_with_na,"Nivel_Educación", "Desconocido")#se puede remplazar ese desconocido por la medio o mediana o valores de tendencia central
        .pipe(fill_in_column_with_na,"Género", "Desconocido")
        .pipe(fill_in_column_with_na, "Edad", data_frame["Edad"].median())
        .pipe(fill_in_column_with_na, "Hijos", data_frame["Hijos"].median())
        .pipe(fill_in_column_with_na, "Ingresos", data_frame["Ingresos"].mean())
        .pipe(fill_in_column_with_na, "Altura", data_frame["Altura"].median())
    )


data_frame = pd.read_csv("dataset_1.csv", index_col = 0)
print(data_frame)

data_frame = pre_data(data_frame)
print(data_frame)