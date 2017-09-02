import random

#Initialize
Events = ['(Empires Event): Triumph', '(Empires Event): Annex',
        '(Empires Event): Donate', '(Empires Event): Advance', 
        '(Adventures Event): Alms', '(Adventures Event): Borrow',
        '(Adventures Event): Quest', '(Adventures Event): Save', 
        '(Empires Event): Delve', '(Adventures Event): Scouting Party',
        '(Empires Event): Tax', '(Adventures Event): Travelling Fair',
        '(Empires Event): Banquet', '(Adventures Event): Bonfire',
        '(Adventures Event): Expedition', '(Adventures Event): Ferry',
        '(Adventures Event): Plan', '(Adventures Event): Mission',
        '(Adventures Event): Pilgrimage', '(Empires Event): Ritual',
        '(Empires Event): Salt the Earth', '(Empires Event): Wedding',
        '(Adventures Event): Ball', '(Adventures Event): Raid',
        '(Adventures Event): Seaway', '(Empires Event): Trade',
        '(Empires Event): Windfall', '(Empires Event): Conquest',
        '(Adventures Event): Lost Arts', '(Adventures Event): Training',
        '(Adventures Event): Inheritance', '(Adventures Event): Pathfinding',
        '(Empires Event): Dominate']

Landmarks = ['(Empires Landmark): Aqueduct', '(Empires Landmark): Arena',
        '(Empires Landmark): Bandit Fort', '(Empires Landmark): Basilica',
        '(Empires Landmark): Baths', '(Empires Landmark): Battlefield',
        '(Empires Landmark): Colonnade', '(Empires Landmark): Defiled Shrine',
        '(Empires Landmark): Fountain', '(Empires Landmark): Keep',
        '(Empires Landmark): Labyrinth', '(Empires Landmark): Mountain Pass',
        '(Empires Landmark): Museum', '(Empires Landmark): Obelisk',
        '(Empires Landmark): Orchard', '(Empires Landmark): Palace',
        '(Empires Landmark): Tomb', '(Empires Landmark): Tower',
        '(Empires Landmark): Triumphal Arch', '(Empires Landmark): Wall',
        '(Empires Landmark): Wolf Den']

Base = ['Base: Cellar', 'Base: Chapel', 'Base: Moat', 'Base: Harbinger',
        'Base: Merchant', 'Base: Village', 'Base: Workshop', 'Base: Vassal',
        'Base: Bureaucrat', 'Base: Gardens', 'Base: Militia',
        'Base: Moneylender', 'Base: Poacher', 'Base: Remodel', 'Base: Remodel',
        'Base: Smithy', 'Base: Throne Room', 'Base: Bandit',
        'Base: Council Room', 'Base: Festival', 'Base: Laboratory',
        'Base: Library', 'Base: Market', 'Base: Mine', 'Base: Sentry',
        'Base: Witch', 'Base: Artisan']

Intrigue = ['Intrigue: Courtyard', 'Intrigue: Lurker', 'Intrigue: Pawn',
        'Intrigue: Masquerade', 'Intrigue: Shanty Town', 'Intrigue: Steward',
        'Intrigue: Swindler', 'Intrigue: Wishing Well', 'Intrigue: Baron',
        'Intrigue: Bridge', 'Intrigue: Conspirator', 'Intrigue: Diplomat',
        'Intrigue: Ironworks', 'Intrigue: Mill', 'Intrigue: Mining Village',
        'Intrigue: Secret Passage', 'Intrigue: Courtier', 'Intrigue: Duke',
        'Intrigue: Minion', 'Intrigue: Patrol', 'Intrigue: Replace',
        'Intrigue: Torturer', 'Intrigue: Trading Post', 'Intrigue: Upgrade',
        'Intrigue: Harem', 'Intrigue: Nobles']

Seaside = ['Seaside: Embargo', 'Seaside: Haven', 'Seaside: Lighthouse',
        'Seaside: Native Village', 'Seaside: Pearl Diver', 'Seaside: Ambassador',
        'Seaside: Fishing Village', 'Seaside: Lookout', 'Seaside: Smugglers',
        'Seaside: Warehouse', 'Seaside: Caravan', 'Seaside: Cutpurse',
        'Seaside: Island', 'Seaside: Navigator', 'Seaside: Pirate Ship',
        'Seaside: Salvager', 'Seaside: Sea Hag', 'Seaside: Treasure Map',
        'Seaside: Bazaar', 'Seaside: Explorer', 'Seaside: Ghost Ship',
        'Seaside: Merchant Ship', 'Seaside: Outpost', 'Seaside: Tactician',
        'Seaside: Treasury', 'Seaside: Wharf']

Alchemy = ['Alchemy: Herbalist', 'Alchemy: Apprentice', 'Alchemy: Transmute',
        'Alchemy: Vineyard', 'Alchemy: Apothecary', 'Alchemy: Scrying Pool',
        'Alchemy: University', 'Alchemy: Alchemist', 'Alchemy: Familiar',
        'Alchemy: Philosopher Stone', 'Alchemy: Golem', 'Alchemy: Possession']

PotionCards = ['Alchemy: Transmute', 'Alchemy: Vineyard', 'Alchemy: Apothecary',
        'Alchemy: Scrying Pool', 'Alchemy: University', 'Alchemy: Alchemist',
        'Alchemy: Familiar', 'Alchemy: Philosopher Stone', 'Alchemy: Golem',
        'Alchemy: Possession']

Prosperity = ['Prosperity: Loan', 'Prosperity: Trade Route',
        'Prosperity: Watchtower', 'Prosperity: Bishop', 'Prosperity: Monument',
        'Prosperity: Quarry', 'Prosperity: Talisman',
        'Prosperity: Worker Village', 'Prosperity: City', 
        'Prosperity: Contraband', 'Prosperity: Counting House',
        'Prosperity: Mint', 'Prosperity: Mountebank', 'Prosperity: Rabble',
        'Prosperity: Royal Seal', 'Prosperity: Vault', 'Prosperity: Venture',
        'Prosperity: Goons', 'Prosperity: Grand Market', 'Prosperity: Hoard',
        'Prosperity: Bank', 'Prosperity: Expand', 'Prosperity: Forge',
        'Prosperity: King Court', 'Prosperity: Peddler']

Cornucopia = ['Cornucopia: Hamlet', 'Cornucopia: Fortune Teller',
        'Cornucopia: Menagerie', 'Cornucopia: Farming Village',
        'Cornucopia: Horse Traders', 'Cornucopia: Remake',
        'Cornucopia: Tournament', 'Cornucopia: Young Witch',
        'Cornucopia: Harvest', 'Cornucopia: Horn of Plenty',
        'Cornucopia: Hunting Party', 'Cornucopia: Jester',
        'Cornucopia: Fairgrounds']

Hinterlands = ['Hinterlands: Crossroads', 'Hinterlands: Duchess',
        'Hinterlands: Fools Gold', 'Hinterlands: Develop', 'Hinterlands: Oasis',
        'Hinterlands: Oracle', 'Hinterlands: Scheme', 'Hinterlands: Tunnel',
        'Hinterlands: Jack of all Trades', 'Hinterlands: Noble Brigand',
        'Hinterlands: Nomad Camp', 'Hinterlands: Silk Road',
        'Hinterlands: Spice Merchant', 'Hinterlands: Trader',
        'Hinterlands: Cache', 'Hinterlands: Cartographer',
        'Hinterlands: Embassy', 'Hinterlands: Haggler', 'Hinterlands: Highway',
        'Hinterlands: Ill-gotten Gains', 'Hinterlands: Inn',
        'Hinterlands: Mandarin', 'Hinterlands: Margrave', 'Hinterlands: Stables',
        'Hinterlands: Border Village', 'Hinterlands: Farmland']

DarkAges = ['Dark Ages: Poor House', 'Dark Ages: Beggar', 'Dark Ages: Squire',
        'Dark Ages: Vagrant', 'Dark Ages: Forager', 'Dark Ages: Hermit',
        'Dark Ages: Market Square', 'Dark Ages: Sage', 'Dark Ages: Storeroom',
        'Dark Ages: Urchin', 'Dark Ages: Armory', 'Dark Ages: Death Cart',
        'Dark Ages: Feodum', 'Dark Ages: Fortress', 'Dark Ages: Ironmonger',
        'Dark Ages: Marauder', 'Dark Ages: Procession', 'Dark Ages: Rats',
        'Dark Ages: Scavenger', 'Dark Ages: Wandering Minstrel',
        'Dark Ages: Band of Misfits', 'Dark Ages: Bandit Camp',
        'Dark Ages: Catacombs', 'Dark Ages: Count', 'Dark Ages: Counterfeit',
        'Dark Ages: Cultist', 'Dark Ages: Graverobber', 'Dark Ages: Junk Dealer',
        'Dark Ages: Knights', 'Dark Ages: Mystic', 'Dark Ages: Pillage',
        'Dark Ages: Rebuild', 'Dark Ages: Rogue', 'Dark Ages: Altar',
        'Dark Ages: Hunting Grounds']

LooterCards = ['Dark Ages: Death Cart', 'Dark Ages: Marauder',
        'Dark Ages: Cultist']

Guilds = ['Guilds: Candlestick Maker', 'Guilds: Stonemason', 'Guilds: Doctor',
        'Guilds: Masterpiece', 'Guilds: Advisor', 'Guilds: Plaza',
        'Guilds: Taxman', 'Guilds: Herald', 'Guilds: Baker', 'Guilds: Butcher',
        'Guilds: Journeyman', 'Guilds: Merchant Guild', 'Guilds: Soothsayer']

Adventures = ['Adventures: Coin of the Realm', 'Adventures: Page',
        'Adventures: Peasant', 'Adventures: Ratcatcher', 'Adventures: Raze',
        'Adventures: Amulet', 'Adventures: Caravan Guard', 'Adventures: Dungeon',
        'Adventures: Gear', 'Adventures: Guide', 'Adventures: Duplicate',
        'Adventures: Magpie', 'Adventures: Messenger', 'Adventures: Miser',
        'Adventures: Port', 'Adventures: Ranger', 'Adventures: Transmogrify',
        'Adventures: Artificer', 'Adventures: Bridge Troll',
        'Adventures: Distant Lands', 'Adventures: Giant',
        'Adventures: Haunted Woods', 'Adventures: Lost Relic',
        'Adventures: Royal Carriage', 'Adventures: Storyteller',
        'Adventures: Swamp Hag', 'Adventures: Treasure Trove',
        'Adventures: Wine Merchant', 'Adventures: Hireling']

Empires = ['Empires: Engineer', 'Empires: City Quarter', 'Empires: Overlord',
        'Empires: Royal Blacksmith', 'Empires: Encampment/Plunder',
        'Empires: Patrician/Emporium', 'Empires: Settlers/Bustling Village',
        'Empires: Castles', 'Empires: Catapult/Rocks', 'Empires: Chariot Race',
        'Empires: Enchantress', 'Empires: Farmers Market',
        'Empires: Gladiator/Fortune', 'Empires: Sacrifice', 'Empires: Temple',
        'Empires: Villa', 'Empires: Archive', 'Empires: Capital',
        'Empires: Charm', 'Empires: Crown', 'Empires: Forum',
        'Empires: Groundskeeper', 'Empires: Legionary', 'Empires: Wild Hunt']

Antiquities = ['Antiquities: Petroglyph', 'Antiquities: Agora',
        'Antiquities: Monolith', 'Antiquities: Aquifer',
        'Antiquities: Tomb Raider', 'Antiquities: Artifact', 'Antiquities: Idol',
        'Antiquities: Digsite', 'Antiquities: Moundbuilder Village',
        'Antiquities: Encroach', 'Antiquities: Stoneworks',
        'Antiquities: Graveyard', 'Antiquities: Inspector',
        'Antiquities: Archaeologist', 'Antiquities: Mission House',
        'Antiquities: Anthropologist', 'Antiquities: Profiteer',
        'Antiquities: Prospector', 'Antiquities: Pyramid', 'Antiquities: Riches',
        'Antiquities: Sarcophagus', 'Antiquities: Shipwreck',
        'Antiquities: Collector', 'Antiquities: Pharaoh',
        'Antiquities: Tomb Guardian', 'Antiquities: Ziggurat']

BaneCards = ['Dark Ages: Vagrant', 'Dark Ages: Squire', 'Dark Ages: Beggar',
        'Hinterlands: Crossroads', 'Hinterlands: Duchess',
        'Hinterlands: Fools Gold', 'Cornucopia: Hamlet', 'Base: Moat',
        'Base: Chapel', 'Base: Cellar', 'Intrigue: Courtyard', 'Intrigue: Lurker',
        'Intrigue: Pawn', 'Seaside: Embargo', 'Alchemy: Herbalist',
        'Seaside: Pearl Diver', 'Seaside: Native Village', 'Seaside: Lighthouse',
        'Seaside: Haven', 'Adventures: Coin of the Realm', 'Adventures: Page',
        'Adventures: Peasant', 'Adventures: Ratcatcher', 'Adventures: Raze',
        'Guilds: Candlestick Maker', 'Guilds: Stonemason',
        'Empires: Settlers/Bustling Village', 'Empires: Patrician/Emporium',
        'Empires: Encampment/Plunder', 'Dark Ages: Urchin',
        'Dark Ages: Storeroom', 'Dark Ages: Sage', 'Dark Ages: Market Square',
        'Dark Ages: Hermit', 'Dark Ages: Forager', 'Hinterlands: Develop',
        'Hinterlands: Oasis', 'Hinterlands: Scheme', 'Hinterlands: Tunnel',
        'Prosperity: Trade Route', 'Prosperity: Watchtower', 'Prosperity: Loan',
        'Cornucopia: Fortune Teller', 'Cornucopia: Menagerie',
        'Intrigue: Masquerade', 'Intrigue: Shanty Town', 'Intrigue: Steward',
        'Intrigue: Swindler', 'Intrigue: Wishing Well', 'Base: Harbinger',
        'Base: Merchant', 'Base: Village', 'Base: Workshop', 'Base: Vassal',
        'Seaside: Fishing Village', 'Seaside: Lookout', 'Seaside: Ambassador',
        'Seaside: Warehouse', 'Seaside: Smugglers', 'Adventures: Amulet',
        'Adventures: Caravan Guard', 'Adventures: Dungeon', 'Adventures: Gear',
        'Adventures: Guide', 'Guilds: Doctor', 'Guilds: Masterpiece',
        'Empires: Castles', 'Empires: Gladiator', 'Empires: Farmers Market',
        'Empires: Encantress', 'Empires: Chariot Race', 'Empires: Catapult',
        'Empires: Catapult/Rocks', 'Empires: Gladiator/Forture',
        'Antiquities: Tomb Raider', 'Antiquities: Moundbuilder Village',
        'Antiquities: Inspector', 'Antiquities: Anthropologist',
        'Antiquties: Prospector', 'Antiquities: Shipwreck',
        'Antiquities: Tomb Guardian']

#Make full list + Events + Landmarks to determine landmarks
completeList = Events + Landmarks + Base + Intrigue + Seaside + Alchemy + \
        Prosperity + Cornucopia + Hinterlands + DarkAges + Guilds + Adventures + \
        Empires + Antiquities

#Check first 2 for Events
random.shuffle(completeList)
tempList = completeList[:4]
eventList = []
for t in tempList:
    if t in Events:
        eventList = eventList + [t]
if len(eventList) > 2:
    eventList = eventList[:2]

#Check first 2 for Landmarks
random.shuffle(completeList)
tempList = completeList[:4]
landmarkList = []
for t in tempList:
    if t in Landmarks:
        landmarkList = landmarkList + [t]
if len(landmarkList) > 2:
    landmarkList = landmarkList[:2]

#Pull cards
pullList = Base + Intrigue + Seaside + Alchemy + Prosperity + Cornucopia + \
        Hinterlands + DarkAges + Guilds + Adventures + Empires + Antiquities
random.shuffle(pullList)
resultList = pullList[:10]

#enforce Alchemy rule
alcCount = 0
for r in resultList:
    if r in Alchemy:
        alcCount = alcCount + 1
if alcCount == 1:
    pullList = Base + Intrigue + Seaside + Prosperity + Cornucopia + \
        Hinterlands + DarkAges + Guilds + Adventures + Empires + Antiquities
    random.shuffle(pullList)
    resultList = pullList[:10]
if alcCount == 2:
    random.shuffle(Alchemy)
    alcList = Alchemy[:3]
    pullList = list(set(pullList) - set(alcList))
    resultList = alcList + pullList[:7]

#Check for Potions
includePotions = set(resultList) & set(PotionCards)
#Check for Shelters
random.shuffle(resultList)
includeShelters = resultList[0] in DarkAges

#Check for Looters
includeLooters = set(resultList) & set(LooterCards)

#Check for Colonies and Platinums
random.shuffle(resultList)
includeColPlat = resultList[0] in Prosperity

#Check for Boulder traps
#Check for Colonies and Platinums
random.shuffle(resultList)
includeBTraps = resultList[0] in Antiquities

#Check for Madman
includeMadman = 'Dark Ages: Hermit' in resultList
#Check for Mercenary
includeMercenary = 'Dark Ages: Urchin' in resultList
#Check for Spoils
includeSpoils = ('Dark Ages: Bandit Camp' in resultList) or \
        ('Dark Ages: Marauder' in resultList) or {'Dark Ages: Pillage'} in resultList

# add Prizes
includePrizes = 'Cornucopia: Tournament' in resultList

# culture deck
includeCulture = 'Antiquities: Anthropologist' in resultList

# create final list
additionalCards = []

if includePotions:
    additionalCards = additionalCards + ['Alchemy: Potions']
if includeShelters:
    additionalCards = additionalCards + ['Dark Ages: Shelters']
if includeLooters:
    additionalCards = additionalCards + ['Dark Ages: Ruins']
if includeColPlat:
    additionalCards = additionalCards + ['Prosperity: Colony',
            'Prosperity: Platinum']
if includeBTraps:
    additionalCards = additionalCards + ['Antiquities: Boulder Traps']
if includeMadman:
    additionalCards = additionalCards + ['Dark Ages: Madman']
if includeMercenary:
    additionalCards = additionalCards + ['Dark Ages: Mercenary']
if includeSpoils:
    additionalCards = additionalCards + ['Dark Ages: Spoils']
if includeCulture:
    additionalCards = additionalCards + ['Culture Deck']

finalResult = list(sorted(resultList + additionalCards))

#Young Witch Support
includeBane = 'Cornucopia: Young Witch' in resultList
if includeBane:
    eligibleBanes = list(set(BaneCards) - set(resultList))
    random.shuffle(eligibleBanes)
    baneCard = ['Bane is ' + eligibleBanes[0]]
    finalResult = finalResult + baneCard

finalResult = finalResult + list(sorted(eventList + landmarkList))

print ('\n'.join(finalResult))