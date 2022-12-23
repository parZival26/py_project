import utils
import charts
import read_csv

data = read_csv.read_csv('./data.csv')

def graph_population():
    labels, values = utils.global_populations(data)
    charts.generate_pie_chart(labels, values)

def graph_country_history():
    new_dict = utils.history_population(data)
    labels = new_dict.keys()
    values = new_dict.values()
    charts.generate_bar_chart(labels, values)

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
    
