# Bottled water + other ingredient(s)
# Use as many functions and operators as possible to learn new coding techniques!

# pot - potion, des - desicion

waterleaf = ['Crate potion', 'Fishing potion', 'Flipper potion', 'Gills potion', 'Greater Luck potion', 'Lesser Luck potion', 'Lifeforce potion', 'Luck potion', 'Obsidian Skin potion', 'Sonar potion', 'Water Walking potion']

ingredient = input('What ingredient would you like to know about? ')

if ingredient == ('waterleaf' or 'water leaf'): print(waterleaf)
wlpotdes = input('What potion would you like to know about? '.lower())

if wlpotdes == ('crate'): print('Amber', 'Moonglow', 'Shiverthorn', 'Waterleaf')
elif wlpotdes == ('fishing'): print('Crispy Honey Block', 'Waterleaf')
elif wlpotdes == ('flipper'): print('Shiverthorn', 'Waterleaf')
elif wlpotdes == ('gills'): print('Waterleaf', 'Coral')
elif wlpotdes == ('greater luck' or 'greaterluck'): print('Waterleaf', 'Ladybug', 'Pink Pearl')
elif wlpotdes == ('lesser luck' or 'lesserluck'): print('Waterleaf', 'Ladybug', 'White Pearl')
elif wlpotdes == ('life force' or 'lifeforce'): print('Prismite', 'Moonglow', 'Shiverthorn', 'Waterleaf')
elif wlpotdes == ('luck'): print('Waterleaf', 'Ladybug', 'Black pearl')
elif wlpotdes == ('obsidian skin' or 'obsidianskin'): print('Fireblossom', 'Waterleaf', 'Obsidian')
elif wlpotdes == ('sonar'): print('Waterleaf', 'Coral')
elif wlpotdes == ('water walking' or 'waterwalking'): print('Waterleaf', 'Shark Fin')
else: print('Would you like to know about a different ingredient? ')
