import requests
from bs4 import BeautifulSoup

url = 'https://www.timeout.com/film/best-movies-of-all-time'

response = requests.get(url)

# change the user agent to avoid 403 error
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Check if the '_zoneItems_882m9_1 zoneItems' div exists on the page
    content_text_div = soup.find(
        'div', {'class': '_zoneItems_882m9_1 zoneItems'})
    if content_text_div:
        # Extract all the paragraph text within the '_zoneItems_882m9_1 zoneItems' div
        paragraphs = content_text_div.find_all(
            'div', {'class': '_title_kc5qn_9'})

        # Print the extracted text
        for paragraph in paragraphs:
            print(paragraph.text)
    else:
        print("Error: '_zoneItems_882m9_1 zoneItems' div not found on the page.")
else:
    print(
        f"Error: Unable to retrieve the page. Status code: {response.status_code}")
