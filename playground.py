import json


flares_description_folder = f"resources/descriptions/flares/"
with open(flares_description_folder + "flares.json", "r") as f:
    j = json.loads(f.read())
    d = {flare['upgraded']+flare['pieces']: flare for flare in j}
    for k, v in d.items():
        d[k] = {
            "upgraded": v["upgraded"],
            "pieces": v["pieces"],
            "pieces_cost": 0,
            "upgraded_cost": 0,
        }

    val_list = list(d.values())
    result = {i: val_list[i] for i in range(len(val_list))}

    with open(flares_description_folder + "flares_set.json", "w") as f2:
        f2.write(json.dumps(result, indent=4))

