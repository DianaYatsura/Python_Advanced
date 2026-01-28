import re
"""
As input data you have list of strings with information about some location:
"id,name,poppulation,is_capital",
"3024,eu_kyiv,24834,y",
"3025,eu_volynia,20231,n"...
Using regular expression write method max_population() for parsing strings 
and get info about location with highest population
"""

def max_population(data):
    city_population = []
    pattern = r"\b([0-9]{4})\D([a-z]\D+)\D([0-9]{4,})\D."
    for match in re.finditer(pattern, str(data)):
        city = match.group(2)
        population = int(match.group(3))
        city_population.append((city, population))

    max_pop = 0
    max_city_data = None

    for city, pop in city_population:
        if pop > max_pop:
            max_pop = pop
            max_city_data = (city, pop)
    return max_city_data


data =  ["id,name,poppulation,is_capital",
"3024,eu_kyiv,24834,y",
"3025,eu_volynia,20231,n",
"3026,eu_galych,23745,n",
"4892,me_medina,18038,n",
"4401,af_cairo,18946,y",
"4700,me_tabriz,13421,n",
"4899,me_bagdad,22723,y",
"6600,af_zulu,09720,n"]

print(max_population(data))   #('eu_kyiv', 24834)



