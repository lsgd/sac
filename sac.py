"""
Prints the SAC sections sorted by yearly membership fees ascending order.
The first number is the yearly membership fee, the number in parenthesis is the one-time fee for becoming a member of this section.

Examples:
    $ python3 sac.py
    $ python3 sac.py family
    $ python3 sac.py youth
    $ python3 sac.py single
"""
import sections
import sys

price_types = ('family', 'youth', 'single')
try:
    selected_type = sys.argv[1]
except IndexError:
    selected_type = price_types[0]

if selected_type not in price_types:
    raise ValueError(f'Selected price type "{selected_type}" does not exist. Pick one of: {", ".join(price_types)}.')

print(f'Selected price type: {selected_type}')
print('=' * 30)

prices = []
for section in sections.prices.get('sectionPrices', []):
    prices.append({
        'cantonId': section.get('cantonId'),
        'name': section.get('name'),
        'price': section.get(selected_type),
    })

for p in sorted(prices, key=lambda x: x['price']['yearly']):
    print(f'{p.get("cantonId")}-{p.get("name")}: {p["price"]["yearly"]} (+{p["price"]["oneTime"]})')