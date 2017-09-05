"""A utitilty to convert custom set data to JSON.

Not really expected to be reused in any other projects.

"""

__all__ = ['ConvertCsvSetToJson']

import csv
import json
import os
import re
import sys
from collections import OrderedDict

reNameAndCost = re.compile(r'(.+)\s+\((\d+)\)')

def ConvertCsvSet(setName, csvfilename):
    setData = OrderedDict([("name", setName), ("cards", [])])

    with open(csvfilename, 'rb') as f:
        reader = csv.reader(f)

        for nameAndCost, cardTypes, rules in reader:
            if not nameAndCost:
                continue

            card = OrderedDict()
            m = reNameAndCost.match(nameAndCost)
            card["name"] = m.group(1)
            card["card-type"] = cardTypes
            card["cost"] = '${}'.format(m.group(2))

            cardRules = re.sub(r'^-{2,}\s*$', '-', rules, flags=re.M)
            card["rules"] = cardRules

            if card:
                setData['cards'].append(card)

    return setData


if __name__ == '__main__':
    fullFileName = sys.argv[1]
    directory, fileName = os.path.split(fullFileName)
    baseName = os.path.splitext(fileName)[0]
    newFileName = os.path.join(directory, baseName + '.json')

    data = ConvertCsvSet(baseName.capitalize(), fullFileName)
    with open(newFileName, 'w') as f:
        json.dump(data, f, indent=4, separators=(',', ': '))