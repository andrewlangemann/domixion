import json
import requests
import urlparse
from bs4 import BeautifulSoup

base_url = r'http://dominion.diehrstraits.com/?set=All&f=list'



def ExtractData():
    data = {}

    with open('dominion-data.html') as f:
        soup = BeautifulSoup(f.read())

    headings = soup.find_all('h2')

    for heading in headings:
        table = heading.find_next_sibling('table')
        for row_index, tr in enumerate(table.find_all('tr')):
            # Skip header row
            if row_index == 0:
                continue

            cardNameCell = tr.find(class_='card-name')
            cardUrl = urlparse.urljoin(base_url, cardNameCell.find('a'))
            cardName = cardNameCell.string
            cardNumber = tr.find(class_='card-number').string


    return data

