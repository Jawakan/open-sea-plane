# Ingredients for potion making
fish = ['Ebonkoi', 'Prismite', 'Shark Fin', 'Doublecod', 'Damselfish', 'Armored Cavefish', 'Crimson Tigerfish', 'Flarefin Koi', 'Obsidifish', 'Prismite', 'Princess Fish', 'Hemopiranha', 'Specular Fish', 'Stinkfish', 'Variegated Lardfish', 'Chaos Fish', 'Frost Minnow']
plants = ['Moonglow', 'Daybloom', 'Deathweed', 'Fireblossom', 'Blinkroot', 'Grass Seeds', 'Shiverthorn', 'Waterleaf', 'Mushroom', 'Glowing Mushroom', 'Cactus', 'Coral']
misc = ['Crispy Honey Block', 'Amber', 'Ladybug', 'Pink Pearl', 'White Pearl', 'Black Pearl', 'Obsidian', 'Gel', 'Pixie Dust', 'Crystal Shard', 'Fallen Star', 'Unicorn Horn', 'Lens']
fragments = ['Nebula Fragment', 'Solar Fragment', 'Stardust Fragment', 'Vortex Fragment']
# Ingredients & Potions lists are incomplete
allpots = ['Crate potion', 'Fishing potion', 'Flipper potion', 'Gills potion', 'Greater Luck potion', 'Lesser Luck potion', 'Life Force potion', 'Luck potion', 'Obsidian Skin potion', 'Sonar potion', 'Water Walking potion', 'Lesser Healing potion', 'Healing potion', 'Lesser Mana potion', 'Greater Healing potion', 'Greater Mana potion']

def help():
    print('\nhelp - opens this menu\nlist - will list all available potion recipies\ncraft - gives helpful instructions on crafting potions\nallheal - lists healing items and their stats\nallmana - lists mana items and their stats\nquit - closes this program\n')

def craft():
    print('\nMost potions can be crafted at a placed bottle.\nTo conserve ingredients, you can craft at an Alchemy Table.\nFlasks can only be crafted at an Imbuing Station.\n')

def potlist():
    allpots.sort()
    for pot in allpots:
        print(pot)

allheal = ('\nLesser Healing potion | +50 HP\nBottled Honey | +80 HP\nRestoration potion | +90 HP\nHealing potion | +100 HP\nGreater Healing potion | +150 HP\nSuper Healing potion | +200 HP\n')
allmana = ('\nLesser Mana potion | +50 Mana\nMana potion | +100 Mana\nGreater Mana potion | +200 Mana\nSuper Mana potion | +300 Mana\nStrange Brew | +400 Mana\n')

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
healpot = allpots[11], plants[9]
greathealpot = misc[8], misc[9]
manapot = allpots[13], plants[9]
superhealpot = allpots[14], fragments[0], fragments[1], fragments[2], fragments[3]
supermanapot = allpots[15], misc[9], misc[10], misc[11]
ammorespot = fish[3], plants[0] # Start checking here
archerypot = plants[1], misc[12]
battlepot = plants[2], 'Vertebra OR Rotten Chunk'
biomesight = plants[3], plants[4], plants[0], plants[5]
builderpot = plants[0], plants[4], plants[6]
calmingpot = fish[4], plants[1]

while True:
    inqpot = input('What potion would you like to know how to make? ').lower() # Inquire potion

    if inqpot == 'crate':
        print(cratepot) # Add formatting to make output pretty if needed
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
    elif inqpot == ('supermana') or inqpot == ('super mana'): 
        print(supermanapot)
    elif inqpot == ('ammoreservation') or inqpot == ('ammo reservation'):
        print(ammorespot)
    elif inqpot == ('archery'):
        print(archerypot)
    elif inqpot == ('battle'):
        print(battlepot)
    elif inqpot == ('biomesight') or inqpot == ('biome sight'):
        print(biomesight)
    elif inqpot == ('build') or inqpot == ('builder'):
        print(builderpot)
    elif inqpot == ('calm') or inqpot == ('calming'):
        print(calmingpot)
    elif inqpot == ('allheal') or inqpot == ('all heal'):
        print(allheal)
    elif inqpot == ('allmana') or inqpot == ('all mana'):
        print(allmana)
    elif inqpot == ('help'):
        help()
    elif inqpot == ('craft') or inqpot == ('crafting'):
        craft()
    elif inqpot == ('list'):
        potlist()
    elif inqpot == ('quit') or inqpot == ('exit'):
        break
    else:
        quit()
