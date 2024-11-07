# Ingredients for potion making
fish = ['Ebonkoi', 'Prismite', 'Shark Fin', 'Doublecod', 'Damselfish', 'Armored Cavefish', 'Crimson Tigerfish', 'Flarefin Koi', 'Obsidifish', 'Prismite', 'Princess Fish', 'Hemopiranha', 'Specular Fish', 'Stinkfish', 'Variegated Lardfish', 'Chaos Fish', 'Frost Minnow']
plants = ['Moonglow', 'Daybloom', 'Deathweed', 'Fireblossom', 'Blinkroot', 'Grass Seeds', 'Shiverthorn', 'Waterleaf', 'Mushroom', 'Glowing Mushroom', 'Cactus', 'Coral']
misc = ['Crispy Honey Block', 'Amber', 'Ladybug', 'Pink Pearl', 'White Pearl', 'Black Pearl', 'Obsidian', 'Gel', 'Pixie Dust', 'Crystal Shard', 'Fallen Star', 'Unicorn Horn']
fragments = ['Nebula Fragment', 'Solar Fragment', 'Stardust Fragment', 'Vortex Fragment']
# Ingredients & Potions lists are incomplete
allpots = ['Crate potion', 'Fishing potion', 'Flipper potion', 'Gills potion', 'Greater Luck potion', 'Lesser Luck potion', 'Life Force potion', 'Luck potion', 'Obsidian Skin potion', 'Sonar potion', 'Water Walking potion', 'Lesser Healing potion', 'Healing potion', 'Lesser Mana potion', 'Greater Healing potion', 'Greater Mana potion']

def help():
    print('help - opens this menu\nlist - will list all available potion recipies\nquit - closes this program')

def potlist():
    allpots.sort()
    for pot in allpots:
        print(pot)

# List of potions
cratepot = misc[1], plants[0], plants[6], plants[7]
fishpot = misc[0], plants[7]
flipperpot = plants[6], plants[7]
gillspot = plants[7], plants[-1]
greaterluckpot = plants[7], misc[2], misc[3]
lesserluckpot = plants[7], misc[2], misc[4]
lifeforcepot = fish[1], plants[0], plants[6], plants[7]
luckpot = plants[7], misc[2], misc[5]
obsidianskinpot = plants[3], plants[7], misc[-1]
sonarpot = plants[7], plants[-1]
waterwalkpot = plants[7], fish[2]
lesshealpot = plants[8], misc[-5], 'Bottle'
healpot = allpots[5], plants[9]
greathealpot = misc[8], misc[9]
manapot = allpots[13], misc[9]
superhealpot = allpots[14], fragments[0], fragments[1], fragments[2], fragments[3]
supermanapot = allpots[15], misc[9], misc[10], misc[11]

while True:
    inqpot = input('What potion would you like to know how to make? ').lower() # Inquire potion

    if inqpot == 'crate':
        print(cratepot) # Add formatting to make pretty if needed
    elif inqpot == 'fishing':
        print(fishpot)
    elif inqpot == 'flipper':
        print(flipperpot)
    elif inqpot == 'gills':
        print(gillspot)
    elif inqpot == ('greaterluck') or inqpot == ('greater luck'):
        print(greaterluckpot)
    elif inqpot == ('lesserluck') or inqpot == ('lesser luck'):
        print(lesserluckpot)
    elif inqpot == ('lifeforce') or inqpot == ('life force'):
        print(lifeforcepot)
    elif inqpot == 'luck':
        print(luckpot)
    elif inqpot == ('obsidianskin') or inqpot == ('obsidian skin'):
        print(obsidianskinpot)
    elif inqpot == 'sonar':
        print(sonarpot)
    elif inqpot == ('waterwalking') or inqpot == ('water walking'):
        print(waterwalkpot)
    elif inqpot == ('lesserhealing') or inqpot == ('lesser healing'):
        print(lesshealpot)
    elif inqpot == ('heal') or inqpot == ('healing'):
        print(healpot)
    elif inqpot == ('greaterhealing') or inqpot == ('greater healing'):
        print(greathealpot)
    elif inqpot == ('mana'):
        print(manapot)
    elif inqpot == ('superhealing') or inqpot == ('super healing'):
        print(superhealpot)
    elif inqpot == ('supermana') or inqpot == ('super mana'): # New potions should be added after the last potion and before non-potion items
        print(supermanapot)                                   # Don't forget to add them to this "allpots" list
    elif inqpot == ('help'):
        help()
    elif inqpot == ('list'):
        potlist()
    elif inqpot == ('quit') or inqpot == ('exit'):
        break
    else:
        quit()
