import requests # for making standard html requests
from bs4 import BeautifulSoup # magical tool for parsing html data
import json # for parsing data
from pandas import DataFrame as df # premier library for data organization
from tabulate import tabulate

page = requests.get("https://location.debonairspizza.co.za/kwazulu-natal/durban")
soup = BeautifulSoup(page.text, 'html.parser')

page = requests.get("https://location.debonairspizza.co.za/kwazulu-natal/durban")
page.encoding = 'ISO-885901'
soup = BeautifulSoup(page.text, 'html.parser')


dollar_tree_list = soup.find_all(class_ = 'c-address-street-1')
city_name_list = soup.find_all(class_ = 'LocationName')

city_adr = []
city = []

n = len(dollar_tree_list)

for i in range(n):
    example = dollar_tree_list[i]
    exp2 = city_name_list[i]
    example_content = example.contents
    exp_content = exp2.contents
    city_adr.append(example_content)    
    city.append(exp_content)

city_address = list(zip(city, city_adr))

# print(df(city_address, columns=['City','Address']))
print(tabulate(city_address, headers=['City', 'Address']))




  