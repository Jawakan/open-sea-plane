# Ingredients for potion making
fish = ['Ebonkoi', 'Prismite', 'Shark Fin', 'Doublecod', 'Damselfish', 'Armored Cavefish', 'Crimson Tigerfish', 'Flarefin Koi', 'Obsidifish', 'Prismite', 'Princess Fish', 'Hemopiranha', 'Specular Fish', 'Stinkfish', 'Variegated Lardfish', 'Chaos Fish', 'Frost Minnow']
plants = ['Moonglow', 'Daybloom', 'Deathweed', 'Fireblossom', 'Blinkroot', 'Grass Seeds', 'Shiverthorn', 'Waterleaf', 'Mushroom', 'Glowing Mushroom', 'Cactus']
misc = ['Crispy Honey Block', 'Amber']
# Ingredients & Potions lists are incomplete

# List of potions
cratepot = misc[1] + plants[0:6-7]
fishpot = misc[0] + plants[7]
flipperpot = plants[6-7]
gillspot = # Finish converting & also make functional
greaterluckpot = ('Waterleaf', 'Ladybug', 'Pink Pearl')
lesserluckpot = ('Waterleaf', 'Ladybug', 'White Pearl')
lifeforcepot = ('Prismite', 'Moonglow', 'Shiverthorn', 'Waterleaf')
luckpot = ('Waterleaf', 'Ladybug', 'Black pearl')
obsidianskinpot = ('Fireblossom', 'Waterleaf', 'Obsidian')
sonarpot = ('Waterleaf', 'Coral')
waterwalkpot = ('Waterleaf', 'Shark Fin')

inqpot = input('What potion would you like to know how to make? ').lower()

if inqpot == 'crate': print(cratepot) # Add formatting to make pretty if needed