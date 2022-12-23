import read_csv

data = read_csv.read_csv('./data.csv')

def global_populations(data):
    continente = input('Elige un continente: ')
    data = list(filter(lambda x: x['Continent'] == continente, data))
    # if continente in data:
    country = list(map(lambda i: i['Country/Territory'], data))
    population = list(map(lambda i: i['World Population Percentage'], data))
        # new_dict = {country: population for (country, population) in zip(country, population)}

        # for (country, population) in zip(country, population):
        #     new_dict[country] = population
    return country, population
    # else:
    #     print('Continente no encontrado')
    #     exit()
    


def history_population(data):
    pais = input('Elige un pais: ')
    new_list = list(filter(lambda x: x['Country/Territory'] == pais, data))
    country_population = [{'1970':  int(x['1970 Population']), 
                                '1980': int(x['1980 Population']), 
                                '1990': int(x['1990 Population']),
                                '2000': int(x['2000 Population']),
                                '2010': int(x['2010 Population']),
                                '2015': int(x['2015 Population']),
                                '2020': int(x['2020 Population']),
                                '2022': int(x['2022 Population'])} for x in new_list]
    country_population = country_population[0]
    return country_population, pais
    
if __name__ == '__main__':
    history_population(data)



