""" generate-card-images.py

To be used with the Dominion Card Image Generator to take JSON card data
and generate URLs for card image generation.

https://shemitz.net/static/dominion3/

"""

import json
import sys
import urllib

c0 = {value: str(i) for i, value in enumerate([
    'Action/Event',
    'Treasure',
    'Victory',
    'Reaction',
    'Duration',
    'Reserve',
    'Curse',
    'Shelter',
    'Ruins',
    'Landmark',
    'CUSTOM'
    ])}


c1 = {value: str(i) for i, value in enumerate([
    'SAME',
    'Action/Event',
    'Treasure',
    'Victory',
    'Reaction',
    'Duration',
    'Reserve',
    'Curse',
    'Shelter',
    'Ruins',
    'Landmark',
    'CUSTOM'
    ])}


def ParseCardColors(card):
    color0 = '0'
    color1 = '0'

    cardType = card['card-type']
    cardTypes = set(cardType.split(' - '))

    if cardTypes >= {'Action', 'Reaction'}:
        color0 = c0['Reaction']
    elif 'Victory' in cardTypes:
        color0 = c0['Victory']
        if 'Action' in cardTypes:
            color1 = c1['Action/Event']
        elif 'Treasure' in cardTypes:
            color1 = c1['Treasure']
    elif 'Treasure' in cardTypes:
        color0 = c0['Treasure']
        if 'Reaction' in cardTypes:
            color1 = c1['Reaction']
    elif cardTypes & {'Curse', 'Boulder'}:
        color0 = c0['Curse']
        if 'Reaction' in cardTypes:
            color1 = c1['Reaction']

    return color0, color1


def GenerateCardImageUrls(fileName, printUrls=True):
    base_url = r'https://shemitz.net/static/dominion3/?{}'
    urls = []

    with open(fileName, 'r') as f:
        setData = json.load(f)

    for card in setData['cards']:
        qs = {}
        qs['title'] = card['name']
        qs['description'] = card['rules']
        qs['type'] = card['card-type']
        qs['price'] = card['cost']

        qs['color0'], qs['color1'] = ParseCardColors(card)

        # Not needed for the card but needed by the generator
        qs['credit'] = ''
        qs['preview'] = ''
        qs['picture'] = ''
        qs['size'] = '0'

        queryString = '&'.join(
                '{}={}'.format(k, urllib.quote(v)) for k, v in qs.iteritems())
        url = base_url.format(queryString)
        urls.append(url)
        if printUrls:
            print url

    return urls


if __name__ == '__main__':
    fileName = sys.argv[1]
    urls = GenerateCardImageUrls(fileName)

    if len(sys.argv) > 2:
        with open(sys.argv[2], 'w') as f:
            for url in urls:
                f.write(url)
                f.write('\n')
