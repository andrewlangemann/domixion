import json
from bs4 import BeautifulSoup

base_url = r'http://dominion.diehrstraits.com/?set=All&f=list'

def ExtractData():
    data = {}

    with open('dominion-data.html') as f:
        soup = BeautifulSoup(f.read())

    headings = soup.find_all('h2')

    for heading in headings:
        table = heading.find_next_sibling('table')
        for row_index, row in enumerate(table.find_all('tr')):
            # Skip header row
            if row_index == 0:
                continue


