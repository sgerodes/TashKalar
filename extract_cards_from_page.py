import json
from models import Faction, NonFactionType

all_types_as_str = set([e.value for e in Faction] + [e.value for e in NonFactionType])


def extract_hand_and_discard():
    with open(f'./game_page.html', 'r') as f:
        for line in f.readlines():
            if 'gameui.completesetup' in line:
                break
        striped = line[line.find('{'):]
        striped = striped[:striped.rfind('}}, {')+2]
        j = json.loads(striped)
        j = {k:v for k,v in j.items() if k in {'hand', 'discard', 'current_tasks', 'next_task', 'claimed'}}

        cards = j.get('hand') + j.get('discard')
        tasks = list()
        flares = list()
        legends = list()
        faction_cards = list()

        if j.get('current_tasks'):
            for t in list(j.get('current_tasks').values()):
                tasks.append({k: v for k, v in t.items() if k in {'type', 'name', 'text'}})
        if j.get('next_task'):
            for t in list(j.get('next_task').values()):
                tasks.append({k: v for k, v in t.items() if k in {'type', 'name', 'text'}})

        for c in cards:
            if c.get('type') == "Flare":
                flares.append({k:v for k,v in c.items() if k in {'type', 'upgraded', 'pieces'}})
            elif c.get('type') == "Legends":
                legends.append({k:v for k,v in c.items() if k in {'type', 'name', 'text'}})
            else:
                faction_cards.append({k:v for k,v in c.items() if k in {'type', 'name', 'text', 'frozentext', 'warptext'}})

        j = {
            'flares': flares,
            'legends': legends,
            'faction_cards': faction_cards,
            'tasks': tasks,
        }



        with open('j.json', 'w') as f2:
           f2.write(json.dumps(j, indent=4))

def extact_g_gamelogs():
    with open(f'./game_page.html', 'r') as f:
        for line in f.readlines():
            if 'g_gamelogs' in line:
                break
        striped = line[line.find('g_gamelogs = {'):]
        striped = striped.replace('g_gamelogs = ', '')
        striped = striped[:-2]

        all_card_jsons = list()

        j = json.loads(striped)



        stack = [j]

        while stack:
            current = stack.pop()
            if isinstance(current, list):
                stack.extend(current)
                continue
            if isinstance(current, dict):
                if current.get('type') and current.get('type') in all_types_as_str:
                    all_card_jsons.append(current)
                else:
                    stack.extend(list(current.values()))



        with open('bkp/descriptions/all_7.json', 'w') as f2:
           f2.write(json.dumps(all_card_jsons, indent=4))

if __name__ == '__main__':
    extact_g_gamelogs()
