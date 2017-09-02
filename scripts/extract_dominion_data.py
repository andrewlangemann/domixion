import json
import re
import requests
import urlparse
from bs4 import BeautifulSoup

base_url = r'http://dominion.diehrstraits.com/?set=All&f=list'


def GetCardImages(setData):
    pass


def ExtractData(getImages=True):
    data = {'sets': []}

    with open('dominion-data.html', 'r') as f:
        soup = BeautifulSoup(f.read())

    headings = soup.find_all('h2')

    for heading in headings:
        setName = re.match(r'Dominion: (.+)', heading.string).group(1)
        setData = {'name': setName, 'cards': []}

        table = heading.find_next_sibling('table')
        for row_index, tr in enumerate(table.find_all('tr')):
            # Skip header row
            if row_index == 0:
                continue

            card = {}

            cardNameCell = tr.find(class_='card-name')
            card['card-url'] = urlparse.urljoin(base_url, cardNameCell.find('a'))
            card['name'] = cardNameCell.string
            card['number'] = tr.find(class_='card-number').string
            card['cost'] = tr.find(class_='card-cost').string
            card['card-type'] = tr.find(class_='card-type').string
            card['rules'] = tr.find(class='card-rules').string
            # Guessing at image url
            imagePath = 'scans/{0}/{1}.jpg'.format(
                    lower(setName), lower(card['name']))
            card['image-url'] = urlparse.urljoin(base_url, imagePath)

            setData['cards'].append(card)

        if getImages:
            GetCardImages(setData)

        data['sets'].append(setData)

    return data


def main():
    data = ExtractData(getImages=False)
    with open('data.json', 'r') as f:
        json.dump(data, f, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    main()