import json
import os
import re
import requests
import urlparse
from bs4 import BeautifulSoup
from collections import OrderedDict

base_url = r'http://dominion.diehrstraits.com/?set=All&f=list'


def GetCardImages(setData):
    folderName = setData['name'].lower().replace(' ', '-')

    for card in setData['cards']:
        r = requests.get(card['image-url'], timeout=2)
        cardImageName = '{}.jpg'.format(card['name'].lower().replace(' ', ''))
        path = os.path.join('images', folderName, cardImageName)
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(path, 'wb') as f:
            f.write(r.content)


def ExtractData(getImages=True):
    data = OrderedDict({'sets': []})

    with open('dominion-data.html', 'r') as f:
        soup = BeautifulSoup(f.read(), 'lxml')

    headings = soup.find_all('h2')

    for heading in headings:
        setName = re.match(r'Dominion: (.+)', heading.string).group(1)
        setData = OrderedDict()
        setData['name'] = setName
        setData['cards'] = []

        table = heading.find_next_sibling('table')
        for row_index, tr in enumerate(table.find_all('tr')):
            # Skip header row
            if row_index == 0:
                continue

            card = OrderedDict()

            card['number'] = tr.find(class_='card-number').string
            cardNameCell = tr.find(class_='card-name')
            card['name'] = cardNameCell.string
            cardLink = cardNameCell.find('a')
            card['card-url'] = urlparse.urljoin(base_url, cardLink['href'])
            card['card-type'] = tr.find(class_='card-type').string
            card['cost'] = tr.find(class_='card-cost').string
            card['rules'] = tr.find(class_='card-rules').string
            # Guessing at image url
            if setName == 'Base Cards':
                imageSetName = 'common'
            else:
                imageSetName = setName.lower()
            imageCardName = card['name'].lower().replace(' ', '')
            imagePath = 'scans/{0}/{1}.jpg'.format(
                    imageSetName, imageCardName)
            card['image-url'] = urlparse.urljoin(base_url, imagePath)

            setData['cards'].append(card)

        if getImages:
            GetCardImages(setData)

        data['sets'].append(setData)

    return data


def main():
    data = ExtractData(getImages=True)
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    main()