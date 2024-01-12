import requests
from bs4 import BeautifulSoup
import pandas as pd


def getAwardedMovies():
    url = 'https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films'
    response = requests.get(url)
    df = pd.DataFrame(columns=['Film', 'Year', 'Awards', 'Nominations'])

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        content_text_div = soup.find(
            'table')
        if content_text_div:
            paragraphs = content_text_div.find_all('tr')

            for i, paragraph in enumerate(paragraphs):
                if (i == 0):
                    continue
                nominations = paragraphs[i].find_all(
                    'td')[3].text.replace('\n', '')
                awards = paragraphs[i].find_all('td')[2].text.split(' ')[0]
                # change awards to int
                awards = int(awards)
                df = pd.concat(
                    [df, pd.DataFrame({'Film': [paragraphs[i].find_all('td')[0].text],
                                       'Year': [paragraphs[i].find_all('td')[1].text],
                                       'Awards': [awards],
                                       'Nominations': [nominations]})], ignore_index=True)
        else:
            print(
                "Error: 'wikitable sortable jquery-tablesorter' table not found on the page.")
            return None
    else:
        print(
            f"Error: Unable to retrieve the page. Status code: {response.status_code}")
        return None

    return df
