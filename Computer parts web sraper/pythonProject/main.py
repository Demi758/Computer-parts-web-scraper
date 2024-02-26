import pandas as pd
from bs4 import BeautifulSoup
import requests

def get_data(computer_part):
    url = "https://gigatron.rs/pretraga?pojam=" + computer_part + "&page=true"
    html = requests.get(url)
    s = BeautifulSoup(html.text, 'html.parser')
    result = s.find(class_="searchpage__main__content__products searchpage__main__content__products--grid")
    results = []
    if(result):
        prices = result.find_all(class_="item__bottom__prices__price")
        names = result.find_all("h4")
        for r in range(0, len(result)):
            results.append(names[r].text)
            results.append(prices[r].text)
    else:
        results.append("No results found.")
        print("No results found.")
    return results

def export(data):
    df = pd.DataFrame(data)
    df.to_excel("Sheet1.xlsx")
    df.to_csv("Sheet1.csv")

name = input("Name of the computer part: ")
data = get_data(name)
export(data)
print("Done.")






