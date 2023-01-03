import read_csv
import pandas as pd

data = read_csv.read_csv('./data.csv')
df = pd.read_csv('./data.csv')


def global_populations(df):
    continente = input('Elige un continente: ')
    # data = list(filter(lambda x: x['Continent'] == continente, data))
    df = df[df['Continent'] == continente]
    # country = list(map(lambda i: i['Country/Territory'], data))
    # population = list(map(lambda i: i['World Population Percentage'], data))
    country = df['Country/Territory'].values
    population = df['World Population Percentage'].values
        # new_dict = {country: population for (country, population) in zip(country, population)}

        # for (country, population) in zip(country, population):
        #     new_dict[country] = population
    return country, population
    # else:
    #     print('Continente no encontrado')
    #     exit()
    


def history_population(df):
    pais = input('Elige un pais: ')
    # new_list = list(filter(lambda x: x['Country/Territory'] == pais, data))
    # country_population = [{'1970':  int(x['1970 Population']), 
    #                             '1980': int(x['1980 Population']), 
    #                             '1990': int(x['1990 Population']),
    #                             '2000': int(x['2000 Population']),
    #                             '2010': int(x['2010 Population']),
    #                             '2015': int(x['2015 Population']),
    #                             '2020': int(x['2020 Population']),
    #                             '2022': int(x['2022 Population'])} for x in new_list]
    # country_population = country_population[0]
    df = df[df['Country/Territory'] == pais]
    country_population = {'1970': int(df['1970 Population'].values), 
                                '1980': int(df['1980 Population'].values), 
                                '1990': int(df['1990 Population'].values),
                                '2000': int(df['2000 Population'].values),
                                '2010': int(df['2010 Population'].values),
                                '2015': int(df['2015 Population'].values),
                                '2020': int(df['2020 Population'].values),
                                '2022': int(df['2022 Population'].values)}    
    return country_population, pais
    
if __name__ == '__main__':
    history_population(df)



