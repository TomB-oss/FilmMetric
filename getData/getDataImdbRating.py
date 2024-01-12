import requests
from bs4 import BeautifulSoup
import pandas as pd


def getRatingByNumberOfRates():
    url = 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm&sort=num_votes%2Cdesc'

    response = requests.get(url)

    df = pd.DataFrame(columns=['Title', 'Year', 'Rating', 'Votes', 'ImageURL'])
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        content_text_div = soup.find(
            'ul', {'class': 'ipc-metadata-list ipc-metadata-list--dividers-between sc-71ed9118-0 kxsUNk compact-list-view ipc-metadata-list--base'})
        if content_text_div:
            paragraphs = content_text_div.find_all('li')

            for i in range(len(paragraphs)):
                pic = paragraphs[i].find_all('img', {
                    'class': 'ipc-image'})
                title = paragraphs[i].find_all('div', {
                    'class': 'ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-935ed930-9 AguIe cli-title'})[0].text
                year = paragraphs[i].find_all('div', {
                    'class': 'sc-935ed930-7 bHIxWH cli-title-metadata'})[0].text[:4]
                if (len(paragraphs[i].find_all('span', {
                        'class': 'ipc-rating-star--voteCount'})) > 0):
                    votes = paragraphs[i].find_all('span', {
                        'class': 'ipc-rating-star--voteCount'})[0].text[2:].replace(')', '')
                else:
                    votes = 'N/A'
                if (len(paragraphs[i].find_all('span', {
                        'class': 'ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating'})) > 0):
                    rating = paragraphs[i].find_all('span', {
                        'class': 'ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating'})[0].text[:3]
                else:
                    rating = 'N/A'
                df = pd.concat(
                    [df, pd.DataFrame({'Title': [title],
                                       'Year': [year],
                                       'Rating': [rating],
                                       'Votes': [votes],
                                       'ImageURL': [pic[0]['src']]})], ignore_index=True)

        else:
            print("Error: '_zoneItems_882m9_1 zoneItems' div not found on the page.")
            return None
    else:
        print(
            f"Error: Unable to retrieve the page. Status code: {response.status_code}")
        return None

    return df


def getImdbRating():
    url = 'https://www.imdb.com/chart/moviemeter/'

    response = requests.get(url)

    df = pd.DataFrame(columns=['Title', 'Year', 'Rating', 'Votes', 'ImageURL'])
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        content_text_div = soup.find(
            'ul', {'class': 'ipc-metadata-list ipc-metadata-list--dividers-between sc-71ed9118-0 kxsUNk compact-list-view ipc-metadata-list--base'})
        if content_text_div:
            paragraphs = content_text_div.find_all('li')

            for i in range(len(paragraphs)):
                pic = paragraphs[i].find_all('img', {
                    'class': 'ipc-image'})
                title = paragraphs[i].find_all('div', {
                    'class': 'ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-935ed930-9 AguIe cli-title'})[0].text
                year = paragraphs[i].find_all('div', {
                    'class': 'sc-935ed930-7 bHIxWH cli-title-metadata'})[0].text[:4]
                if (len(paragraphs[i].find_all('span', {
                        'class': 'ipc-rating-star--voteCount'})) > 0):
                    votes = paragraphs[i].find_all('span', {
                        'class': 'ipc-rating-star--voteCount'})[0].text[2:].replace(')', '')
                else:
                    votes = 'N/A'
                if (len(paragraphs[i].find_all('span', {
                        'class': 'ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating'})) > 0):
                    rating = paragraphs[i].find_all('span', {
                        'class': 'ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating'})[0].text[:3]
                else:
                    rating = 'N/A'
                df = pd.concat(
                    [df, pd.DataFrame({'Title': [title],
                                       'Year': [year],
                                       'Rating': [rating],
                                       'Votes': [votes],
                                       'ImageURL': [pic[0]['src']]})], ignore_index=True)

        else:
            print("Error: '_zoneItems_882m9_1 zoneItems' div not found on the page.")
            return None
    else:
        print(
            f"Error: Unable to retrieve the page. Status code: {response.status_code}")
        return None

    return df
