from PIL import Image
import os
from cards_pictures_order import cards_pictures_order, cards_pictures_stats, cards_manual_metadata_ordered
from functools import reduce
import json
from collections import defaultdict
from models import *
import logging
import os


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# logging.basicConfig(level=logging.DEBUG)


tasks_count = 24
faction_card_count = 18
legend_count = 12
flares_count = 12
pictures_folder = 'resources/pictures'
ranked_pictures_path = f'{pictures_folder}/ranked'
combined_pictures_path = f'{pictures_folder}/combined'
description_folder = 'resources/descriptions'
factions_original = (Faction.SYLVAN, Faction.SOUTHERN, Faction.NORTHERN, Faction.HIGHLAND,
                     Faction.EVERFROST, Faction.NETHERVOID, Faction.ETHERWEAVE)
factions_imperial_combined = (Faction.SYLVAN, Faction.IMPERIAL, Faction.HIGHLAND,
                              Faction.EVERFROST, Faction.NETHERVOID, Faction.ETHERWEAVE)
factions_all = (Faction.SYLVAN,  Faction.SOUTHERN, Faction.NORTHERN, Faction.IMPERIAL, Faction.HIGHLAND,
                              Faction.EVERFROST, Faction.NETHERVOID, Faction.ETHERWEAVE)
imperial_factions = {Faction.SOUTHERN.value, Faction.NORTHERN.value, Faction.IMPERIAL.value}


def split_into_singles():
    for file_name in os.listdir(pictures_folder):
        if not file_name.endswith('_big.webp'):
            continue
        card_width = 250
        if file_name.startswith('tasks'):
            card_width = 9744 // tasks_count

        name_of_card_type = file_name.replace('_big.webp', '')
        big_image_path = f'{pictures_folder}/{file_name}'

        im = Image.open(big_image_path)
        width, height = im.size
        destination_folder = f"{pictures_folder}/single_cards/{name_of_card_type}"
        create_new_folder(destination_folder)
        for i in range(width//card_width):
            cropped = im.crop((card_width * i, 0, card_width * (i + 1), height))
            new_picture_name = cards_pictures_order[name_of_card_type][i] if name_of_card_type in cards_pictures_order else f"{name_of_card_type}_{i}"
            new_picture_relative_path= f"{destination_folder}/{new_picture_name}.webp"
            cropped.save(new_picture_relative_path)


def create_new_folder(folder_name):
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, folder_name)
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)


def concat_images_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, max(im1.height, im2.height)))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


def concat_images_v(im1, im2):
    dst = Image.new('RGB', (max(im1.width, im2.width), im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst


def create_combined_picture():
    create_new_folder(combined_pictures_path)
    pil_images = [Image.open(f'{pictures_folder}/{f.value}_big.webp') for f in factions_imperial_combined]
    combined_image = reduce(concat_images_v, pil_images)
    combined_image.save(f'{combined_pictures_path}/combined.webp')


def get_card_image_from_big_image(faction: str, card_name: str):
    cards_order = cards_pictures_order[faction]
    big_pil_image = Image.open(f'{pictures_folder}/{faction}_big.webp')
    card_order_number = cards_order.index(card_name)

    card_width = 250
    height = big_pil_image.height
    return big_pil_image.crop((card_width * card_order_number, 0, card_width * (card_order_number + 1), height))


def create_card_old(faction:str, card_name:str) -> Card:
    cards_jsons_dict = get_fetched_metadata(faction)
    card_stats = cards_pictures_stats[faction]
    card = Card()
    card.name = card_name
    card.faction = faction
    card.cost = card_stats.get(card_name).get('cost')
    card.pilImage = get_card_image_from_big_image(faction, card_name)

    if faction == Faction.SOUTHERN.value or faction == Faction.NORTHERN.value:
        nor_card_json = get_fetched_metadata(Faction.NORTHERN.value).get(card_name)
        sou_card_json = get_fetched_metadata(Faction.SOUTHERN.value).get(card_name)
        card_json = nor_card_json or sou_card_json
    else:
        card_json = cards_jsons_dict.get(card_name) if cards_jsons_dict else None

    if card_json:
        card.text = card_json.get('text')
        if 'warptext' in card_json:
            card.special_text = card_json.get('warptext')
            card.special_text_type = SpecialTextType.WARP_TEXT
        elif 'frozentext' in card_json:
            card.special_text = card_json.get('frozentext')
            card.special_text_type = SpecialTextType.FROZEN_TEXT
    else:
        logger.warning(f'No card description for {faction}/{card_name}')

    return card


def create_card(type: str, card_name: str) -> Card:
    cards_jsons_dict = get_fetched_metadata(type)
    cards_metadata = cards_manual_metadata_ordered[type]

    if type in factions_original or type == Faction.IMPERIAL.value:
        card = CreatureCard()
        # TODO
    elif type == NonFactionType.LEGEND.value:
        card = LegendaryCard()
        card.name = card_name
        card.text = cards_jsons_dict.get(card_name).get('text')
        # TOD
    elif type == NonFactionType.TASK.value:
        card = TaskCard()
        # TODO
    elif type == NonFactionType.FLARE.value:
        card = FlareCard()
        # TODO
    else:
        logger.warning(f'Type {type} is not known')
        raise RuntimeError()

    # card.pilImage = get_card_image_from_big_image(faction, card_name)


def get_fetched_metadata(faction):
    important_card_json_keys = {'type', 'name', 'text', 'warptext', 'frozentext'}
    def filter_only_important_data(card_json):
        return {k: v for k, v in card_json.items() if k in important_card_json_keys}

    if faction in imperial_factions:
        paths = [
            f'{description_folder}/{Faction.SOUTHERN.value}.json',
            f'{description_folder}/{Faction.NORTHERN.value}.json',
            f'{description_folder}/{Faction.IMPERIAL.value}.json',
        ]
        cards_jsons = dict()
        for file in paths:
            if os.path.exists(file):
                with open(file, 'r') as f:
                    description_json = json.loads(f.read())
                    local_cards_jsons = description_json.get('hand') + description_json.get('discard')
                    if description_json.get('faction_cards'):
                        local_cards_jsons += description_json.get('faction_cards')
                    local_cards_jsons = list(filter(lambda card: card.get('type') in imperial_factions, local_cards_jsons))
                    cards_jsons.update({j['name']: {**filter_only_important_data(j), 'type': 'Imperial'} for j in local_cards_jsons})
        if not cards_jsons:
            logger.warning(f'Not found description jsons for {faction}')
        return cards_jsons
    elif faction is NonFactionType.LEGEND.value:
        file_path = f'{description_folder}/legends/{NonFactionType.LEGEND.value}.json'
        if not os.path.exists(file_path):
            logger.warning(f'Not found description jsons for {faction}')
            return None
        with open(file_path, 'r') as f:
            description_json = json.loads(f.read())
            return {j['name']: j for j in description_json}
    else:
        file_path = f'{description_folder}/{faction}.json'
        logger.info(f'Reading json of faction {faction} at {file_path}')
        if not os.path.exists(file_path):
            logger.warning(f'Not found description jsons for {faction}')
            return None
        with open(file_path, 'r') as f:
            description_json = json.loads(f.read())
            cards_jsons = description_json.get('hand') + description_json.get('discard')
            if description_json.get('faction_cards'):
                cards_jsons += description_json.get('faction_cards')
            cards_jsons = list(filter(lambda card: card.get('type') == faction, cards_jsons))
            return {j['name']: filter_only_important_data(j) for j in cards_jsons} #{j['name']: j for j in cards_jsons}


def create_ranked_pictures():
    create_new_folder(ranked_pictures_path)

    for faction_enum in (Faction.ETHERWEAVE, Faction.IMPERIAL):
        faction = faction_enum.value
        faction_cards = list()
        card_order = cards_pictures_order[faction]
        for card_name in card_order:
            faction_cards.append(create_card(faction, card_name))

        min_level = reduce(lambda a, b: min(a, b), map(lambda card: card.cost, faction_cards))
        max_level = reduce(lambda a, b: max(a, b), map(lambda card: card.cost, faction_cards))

        cost_to_cards = defaultdict(list)
        for card in faction_cards:
            cost_to_cards[card.cost].append(card)

        image_rows = list()
        for cost in range(min_level, max_level+1):
            current_cost_cards = list(cost_to_cards.get(cost))
            img_row = current_cost_cards.pop(0).pilImage
            while current_cost_cards:
                img_row = concat_images_h(img_row, current_cost_cards.pop(0).pilImage)
            image_rows.append(img_row)

        full_image = image_rows.pop(0)
        while image_rows:
            full_image = concat_images_v(full_image, image_rows.pop(0))

        full_image.save(f'{ranked_pictures_path}/{faction}_ranked.webp')

def create_ranked_legends():
    create_new_folder(ranked_pictures_path)
    legend_str = NonFactionType.LEGEND.value
    legend_cards = list()
    legends_metadata_ordered = cards_manual_metadata_ordered[legend_str]
    for l in legends_metadata_ordered:
        card_name = l.get('name')





def combine_imperial():
    def get_half_of_picture(pil_image, direction):
        # direction should be in ('top', 'bottom', 'left', 'right')
        width, height = pil_image.size
        # The crop rectangle, as a (left, upper, right, lower)-tuple.
        if direction == 'top':
            return pil_image.crop((0, height // 2, width, height))
        elif direction == 'bottom':
            return pil_image.crop((0, 0, width, height // 2))
        elif direction == 'left':
            return pil_image.crop((width // 2, 0, width, height))
        elif direction == 'right':
            return pil_image.crop((0, 0, width // 2, height))

    imperial_cards = list()
    for faction in (Faction.NORTHERN, Faction.SOUTHERN):
        faction_str = faction.value
        faction_cards = list()
        card_order = cards_pictures_order[faction_str]
        for card_name in card_order:
            faction_cards.append(create_card(faction_str, card_name))
        imperial_cards.append(faction_cards)

    combined_set_image = None
    for southern_card, northern_card in zip(imperial_cards[0], imperial_cards[1]):
        # top_card = get_half_of_picture(northern_card.pilImage, "top")
        # bottom_card = get_half_of_picture(southern_card.pilImage, "bottom")
        # combined_card_image = concat_images_v(bottom_card, top_card)
        left_card = get_half_of_picture(northern_card.pilImage, "left")
        right_card = get_half_of_picture(southern_card.pilImage, "right")
        combined_card_image = concat_images_h(right_card, left_card)
        if not combined_set_image:
            combined_set_image = combined_card_image
        else:
            combined_set_image = concat_images_h(combined_set_image, combined_card_image)
    combined_set_image.save(f'{pictures_folder}/Imperial_big.webp')
    # combined_set_image.show()


if __name__ == '__main__':
    # Highland Not all cards present. Is 16, Should 18
    # Sylvan Not all cards present. Is 15, Should 18
    # NETHERVOID Not all cards present. Is 14, Should 18
    card_type = Faction.HIGHLAND
    if card_type in factions_all:
        card_count = faction_card_count
    elif card_type == NonFactionType.LEGEND.value:
        card_count = legend_count
    elif card_type == NonFactionType.FLARE.value:
        card_count = flares_count
    elif card_type == NonFactionType.TASK.value:
        card_count = tasks_count
    else:
        raise RuntimeError(f'Not known card_type: {card_type}')

    faction_str = card_type.value
    fetched_metadata = get_fetched_metadata(faction_str)
    if len(fetched_metadata) < card_count:
        print(f'Not all cards present. Is {len(fetched_metadata)}, Should {card_count}')
    print(fetched_metadata)
    with open(f'resources/descriptions/{faction_str}_2.json', "w") as f:
        f.write(json.dumps(fetched_metadata, indent=4))

