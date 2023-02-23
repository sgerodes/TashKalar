import json
from cards_pictures_order import cards_pictures_order

def read_legends():
    with open(f'resources/descriptions/legends/legends.json', 'r') as f:
        j = json.loads(f.read())
        legend_set = {l['name'] for l in j}
        for l in legend_set:
            print(f'"{l}",')

def reformat_legend():
    cpo = cards_pictures_order.get('Legend')
    for c in cpo:
        print(f'\t\t{{\n\t\t\t"name": "{c}",\n\t\t\t"common_cost": 0,\n\t\t\t"upgraded_cost": 0,\n\t\t}},')


