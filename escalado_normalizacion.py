import numpy as np
import matplotlib.pyplot as plt

#vamos a usar una data aleatoria para un ejemplo de escalado y normalizacion de datos

data = np.random.rand(1000)*100 - 50
#plt.plot(data)
#plt.show()

# funcion para tener los datos en una escala de 0 a 1 
def min_max_scaler(data):
    data_min = np.min(data)
    data_max = np.max(data)

    data_scaler = (data - data_min) / (data_max - data_min)

    return data_scaler

norm_data = min_max_scaler(data)
#plt.plot(norm_data)
#plt.show()

def standar_scaler(data):
    media = np.mean(data)
    standar_deviation = np.std(data)

    data_standar = (data - media) / standar_deviation
    return data_standar

std_data = standar_scaler(data)
plt.plot(std_data)
plt.show()
