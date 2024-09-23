# Bottled water + other ingredient(s)

# pot - potion, des - desicion

cratepot = ('Amber', 'Moonglow', 'Shiverthorn', 'Waterleaf')
fishpot = ('Crispy Honey Block', 'Waterleaf')
flipperpot = ('Shiverthorn', 'Waterleaf')
gillspot = ('Waterleaf', 'Coral')
greaterluckpot = ('Waterleaf', 'Ladybug', 'Pink Pearl')
lesserluckpot = ('Waterleaf', 'Ladybug', 'White Pearl')
lifeforcepot = ('Prismite', 'Moonglow', 'Shiverthorn', 'Waterleaf')
luckpot = ('Waterleaf', 'Ladybug', 'Black pearl')
obsidianskinpot = ('Fireblossom', 'Waterleaf', 'Obsidian')
sonarpot = ('Waterleaf', 'Coral')
waterwalkpot = ('Waterleaf', 'Shark Fin')

waterleaf = ['Crate potion', 'Fishing potion', 'Flipper potion', 'Gills potion', 'Greater Luck potion', 'Lesser Luck potion', 'Lifeforce potion', 'Luck potion', 'Obsidian Skin potion', 'Sonar potion', 'Water Walking potion']

ingredient = input('What ingredient would you like to know about? ')

if ingredient == ('waterleaf') or ('water leaf'): print(waterleaf)
wlpotdes = input('What potion would you like to know about? ').lower()

if wlpotdes == ('crate'): print(', '.join(cratepot))
elif wlpotdes == ('fishing'): print(', '.join(fishpot))
elif wlpotdes == ('flipper'): print(', '.join(flipperpot))
elif wlpotdes == ('gills'): print(', '.join(gillspot))
elif wlpotdes == ('greater luck') or ('greaterluck'): print(', '.join(greaterluckpot)) # or function not working as expected
elif wlpotdes == ('lesser luck') or ('lesserluck'): print(', '.join(lesserluckpot))
elif wlpotdes == ('life force') or ('lifeforce'): print(', '.join(lifeforcepot))
elif wlpotdes == ('luck'): print(', '.join(luckpot))
elif wlpotdes == ('obsidian skin') or ('obsidianskin'): print(', '.join(obsidianskinpot))
elif wlpotdes == ('sonar'): print(', '.join(sonarpot))
elif wlpotdes == ('water walking') or ('waterwalking'): print(', '.join(waterwalkpot))
else: print('Would you like to know about a different ingredient? ')

# I'm starting to think it would've made more sense to ask which potion instead
# then give a list of ingredients needed for that potion
