import utils
import charts
import read_csv
import pandas as pd

data = read_csv.read_csv('./data.csv')
df = pd.read_csv('./data.csv')

def graph_population():
    labels, values = utils.global_populations(df)
    charts.generate_pie_chart(labels, values)

def graph_country_history():
    new_tuple = utils.history_population(df)
    new_dict = new_tuple[0]
    labels = new_dict.keys()
    values = new_dict.values()
    pais = new_tuple[1]
    charts.generate_bar_chart(pais, labels, values)

def run():
    elige = int(input("""Bienvenido al graficador de pobalcion
    (1)Graficar la poblacion de un continente
    (2)Graficar la poblacion de la historia de un pais
    Elige una opcion: """))  
    if elige  == 1:
        graph_population()
    elif elige == 2:
        graph_country_history()
    else:
        print("Elige una opcion valida")



if __name__ == '__main__':
   run()
    
