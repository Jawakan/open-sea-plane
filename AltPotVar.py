# Ingredients for potion making
fish = ['Ebonkoi', 'Prismite', 'Shark Fin', 'Doublecod', 'Damselfish', 'Armored Cavefish', 'Crimson Tigerfish', 'Flarefin Koi', 'Obsidifish', 'Prismite', 'Princess Fish', 'Hemopiranha', 'Specular Fish', 'Stinkfish', 'Variegated Lardfish', 'Chaos Fish', 'Frost Minnow']
plants = ['Moonglow', 'Daybloom', 'Deathweed', 'Fireblossom', 'Blinkroot', 'Grass Seeds', 'Shiverthorn', 'Waterleaf', 'Mushroom', 'Glowing Mushroom', 'Cactus', 'Coral']
misc = ['Crispy Honey Block', 'Amber', 'Ladybug', 'Pink Pearl', 'White Pearl', 'Black Pearl', 'Obsidian', 'Gel', 'Pixie Dust', 'Crystal Shard', 'Fallen Star', 'Unicorn Horn', 'Lens', 'Cobweb', 'Feather']
fragments = ['Nebula Fragment', 'Solar Fragment', 'Stardust Fragment', 'Vortex Fragment']
# Ingredients & Potions lists are incomplete
allpots = ['Crate potion', 'Fishing potion', 'Flipper potion', 'Gills potion', 'Greater Luck potion', 'Lesser Luck potion', 'Life Force potion', 'Luck potion', 'Obsidian Skin potion', 'Sonar potion', 'Water Walking potion', 'Lesser Healing potion', 'Healing potion', 'Greater Healing potion', 'Mana potion', 'Super Healing potion', 'Super Mana potion', 'Ammo Reservation potion', 'Archery potion', 'Battle potion', 'Biome Sight potion', 'Builder potion', 'Calming potion', 'Danger Sense potion', 'Endurance potion', 'Featherfall potion', 'Gravitational potion', 'Heartreach potion', 'Hunter potion', 'Inferno potion', 'Invisibility potion', 'Regeneration potion', 'Swiftness potion', 'Night Owl potion']

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
cratepot = (misc[1], plants[0], plants[6], plants[7])
fishpot = (misc[0], plants[7])
flipperpot = (plants[6], plants[7])
gillspot = (plants[7], plants[-1])
greaterluckpot = (plants[7], misc[2], misc[3])
lesserluckpot = (plants[7], misc[2], misc[4])
lifeforcepot = (fish[1], plants[0], plants[6], plants[7])
luckpot = (plants[7], misc[2], misc[5])
obsidianskinpot = (plants[3], plants[7], misc[-1])
sonarpot = (plants[7], plants[-1])
waterwalkpot = (plants[7], fish[2])
lesshealpot = (plants[8], misc[-5], 'Bottle')
healpot = (allpots[11], plants[9])
greathealpot = (misc[8], misc[9])
manapot = (allpots[13], plants[9])
superhealpot = (allpots[14], fragments[0], fragments[1], fragments[2], fragments[3])
supermanapot = (allpots[15], misc[9], misc[10], misc[11])
ammorespot = (fish[3], plants[0])
archerypot = (plants[1], misc[12])
battlepot = (plants[2], 'Vertebra/Rotten Chunk')
biomesight = (plants[3], plants[4], plants[0], plants[5])
builderpot = (plants[0], plants[4], plants[6])
calmingpot = (fish[4], plants[1])
dangersensepot = (plants[6], misc[13])
endurancepot = (fish[5], plants[4])
featherfallpot = (plants[1], plants[4], misc[14])
gravitypot = (plants[3], plants[2], plants[4], misc[14]) # Gravity turned off with Python :)
heartreachpot = (fish[6], plants[1])
hunterpot = (plants[1], plants[4], fish[2])
infernopot = (fish[7], fish[8], plants[3])
invisibilitypot = (plants[4], plants[0])
regenpot = (plants[1], plants[8])
swiftpot = (plants[4], plants[-2])
nightowlpot = (plants[1], plants[4])

while True:
    inqpot = input('What potion would you like to know how to make? ').lower() # Inquire potion

    if inqpot == 'crate':
        print('\n', ', '.join(cratepot), '\n')
    elif inqpot == 'fishing':
        print('\n', ', '.join(fishpot), '\n')
    elif inqpot == 'flipper':
        print('\n', ', '.join(flipperpot), '\n')
    elif inqpot == 'gills':
        print('\n', ', '.join(gillspot), '\n')
    elif inqpot == ('greaterluck') or inqpot == ('greater luck'):
        print('\n', ', '.join(greaterluckpot), '\n')
    elif inqpot == ('lesserluck') or inqpot == ('lesser luck'):
        print('\n', ', '.join(lesserluckpot), '\n')
    elif inqpot == ('lifeforce') or inqpot == ('life force'):
        print('\n', ', '.join(lifeforcepot), '\n')
    elif inqpot == 'luck':
        print('\n', ', '.join(luckpot), '\n')
    elif inqpot == ('obsidianskin') or inqpot == ('obsidian skin'):
        print('\n', ', '.join(obsidianskinpot), '\n')
    elif inqpot == 'sonar':
        print('\n', ', '.join(sonarpot), '\n')
    elif inqpot == ('waterwalking') or inqpot == ('water walking'):
        print('\n', ', '.join(waterwalkpot), '\n')
    elif inqpot == ('lesserhealing') or inqpot == ('lesser healing'):
        print('\n', ', '.join(lesshealpot), '\n')
    elif inqpot == ('heal') or inqpot == ('healing'):
        print('\n', ', '.join(healpot), '\n')
    elif inqpot == ('greaterhealing') or inqpot == ('greater healing'):
        print('\n', ', '.join(greathealpot), '\n')
    elif inqpot == ('mana'):
        print('\n', ', '.join(manapot), '\n')
    elif inqpot == ('superhealing') or inqpot == ('super healing'):
        print('\n', ', '.join(superhealpot), '\n')
    elif inqpot == ('supermana') or inqpot == ('super mana'): 
        print('\n', ', '.join(supermanapot), '\n')
    elif inqpot == ('ammoreservation') or inqpot == ('ammo reservation'):
        print('\n', ', '.join(ammorespot), '\n')
    elif inqpot == ('archery'):
        print('\n', ', '.join(archerypot), '\n')
    elif inqpot == ('battle'):
        print('\n', ', '.join(battlepot), '\n')
    elif inqpot == ('biomesight') or inqpot == ('biome sight'):
        print('\n', ', '.join(biomesight), '\n')
    elif inqpot == ('build') or inqpot == ('builder'):
        print('\n', ', '.join(builderpot), '\n')
    elif inqpot == ('calm') or inqpot == ('calming'):
        print('\n', ', '.join(calmingpot), '\n')
    elif inqpot == ('dangersense') or inqpot == ('danger sense'):
        print('\n', ', '.join(dangersensepot), '\n')
    elif inqpot == ('endurance'):
        print('\n', ', '.join(endurancepot), '\n')
    elif inqpot == ('featherfall') or inqpot == ('feather fall'):
        print('\n', ', '.join(featherfallpot), '\n')
    elif inqpot == ('gravity') or inqpot == ('gravitational'):
        print('\n', ', '.join(gravitypot), '\n')
    elif inqpot == ('heartreach') or inqpot == ('heart reach'):
        print('\n', ', '.join(heartreachpot), '\n')
    elif inqpot == ('hunter'):
        print('\n', ', '.join(hunterpot), '\n')
    elif inqpot == ('inferno'):
        print('\n', ', '.join(infernopot), '\n')
    elif inqpot == ('invisible') or inqpot == ('invisibility'):
        print('\n', ', '.join(invisibilitypot), '\n')
    elif inqpot == ('regen') or inqpot == ('regeneration'):
        print('\n', ', '.join(regenpot), '\n')
    elif inqpot == ('swift') or inqpot == ('swiftness'):
        print('\n', ', '.join(swiftpot), '\n')
    elif inqpot == ('night owl') or inqpot == ('nightowl'):
        print('\n', ', '.join(nightowlpot), '\n')
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
        print('Invalid input')

# Wishlist - Add quantities of items needed for potions & number of potions created from recipe
# Add more info. once all potions are added and verified as correct - useful feature ideas go here
# Add general descriptions of potions with maybe "crate potion des" OR effects of all potions starting with the letter "I" 
# Ex: command | "potion des" - please select a letter; command | "i" - inferno, invisibility, etc. along with a description of each (Horizontal layout of each line)
# Add If "Invalid input" is output 3 times (every 3 times) then Output message 'Type: "help" for a list of commands'
