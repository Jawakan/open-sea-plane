import random

bossdrop = ['Rare item A', 'Rare item B', 'Rare item C']
thebossdrop = ('Rare item A', 'Rare item B', 'Rare item C')
#sarcasm = ("I have one but it's mine.")

random.shuffle(bossdrop)
bossitem = bossdrop.pop()

whatsay = (f"Oh, I have a {thebossdrop[0]}. But it's mine.")
whatthink = (f'I have a {bossitem}')

print(f'Can I have a {thebossdrop[0]}?')

if thebossdrop[0] == bossitem: print(whatsay)
else: print(whatthink)
# Define sarcasm formatting and pass the  sarcasm variable to re_sarcasm
if bossitem == "Rare item A": re_sarcasm = print('i HaVe OnE bUt ItS mInE.')
else: re_explain = print("That's not what I need")
