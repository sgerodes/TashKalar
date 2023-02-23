import json


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

    for t in list(j.get('current_tasks').values()) + list(j.get('next_task').values()):
        tasks.append({k:v for k,v in t.items() if k in {'type', 'name', 'text'}})

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
