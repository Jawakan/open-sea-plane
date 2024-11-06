# Ingredients for potion making
fish = ['Ebonkoi', 'Prismite', 'Shark Fin', 'Doublecod', 'Damselfish', 'Armored Cavefish', 'Crimson Tigerfish', 'Flarefin Koi', 'Obsidifish', 'Prismite', 'Princess Fish', 'Hemopiranha', 'Specular Fish', 'Stinkfish', 'Variegated Lardfish', 'Chaos Fish', 'Frost Minnow']
plants = ['Moonglow', 'Daybloom', 'Deathweed', 'Fireblossom', 'Blinkroot', 'Grass Seeds', 'Shiverthorn', 'Waterleaf', 'Mushroom', 'Glowing Mushroom', 'Cactus', 'Coral']
misc = ['Crispy Honey Block', 'Amber', 'Ladybug', 'Pink Pearl', 'White Pearl', 'Black Pearl', 'Obsidian', 'Gel', 'Pixie Dust', 'Crystal Shard']

allpots = ['Crate potion', 'Fishing potion', 'Flipper potion', 'Gills potion', 'Greater Luck potion', 'Lesser Luck potion', 'Life Force potion', 'Luck potion', 'Obsidian Skin potion', 'Sonar potion', 'Water Walking potion', 'Lesser Healing potion', 'Healing potion']
# Ingredients & Potions lists are incomplete

# List of potions
cratepot = misc[1], plants[0], plants[6], plants[7]
fishpot = misc[0], plants[7]
flipperpot = plants[6], plants[7]
gillspot = plants[7], plants[-1]
greaterluckpot = plants[7], misc[2], misc[3] # Printing by default if no input is given? & for any variable past this
lesserluckpot = plants[7], misc[2], misc[4]
lifeforcepot = fish[1], plants[0], plants[6], plants[7]
luckpot = plants[7], misc[2], misc[5]
obsidianskinpot = plants[3], plants[7], misc[-1]
sonarpot = plants[7], plants[-1]
waterwalkpot = plants[7], fish[2]
lesshealpot = plants[8], misc[-1], 'Bottle'
healpot = allpots[5], plants[9]
greathealpot = misc[8], misc[9]

def allpotion():
    print(allpots)

inqpot = input('What potion would you like to know how to make? ').lower() # Inquire potion

if inqpot == 'crate':
    print(cratepot) # Add formatting to make pretty if needed
elif inqpot == 'fishing':
    print(fishpot)
elif inqpot == 'flipper':
    print(flipperpot)
elif inqpot == 'gills':
    print(gillspot)
elif inqpot == ('greaterluck' or 'greater luck'):
    print(greaterluckpot)
elif inqpot == ('lesserluck' or 'lesser luck'):
    print(lesserluckpot)
elif inqpot == ('lifeforce' or 'life force'):
    print(lifeforcepot)
elif inqpot == 'luck':
    print(luckpot)
elif inqpot == ('obsidianskin' or 'obsidian skin'):
    print(obsidianskinpot)
elif inqpot == 'sonar':
    print(sonarpot)
elif inqpot == ('waterwalking' or 'water walking'):
    print(waterwalkpot)
elif inqpot == ('lesserhealing' or 'lesser healing'):
    print(lesshealpot)
elif inqpot == ('heal' or 'healing'):
    print(healpot)
elif inqpot == ('greaterhealing' or 'greater healing'):
    print(greathealpot)
else:
    inqelse = print('Would you like to know about a different potion? '.lower()) # Inquire else

    if inqelse == ('y' or 'yes'): print("Return to top") #Make return to top
    else: quit()
