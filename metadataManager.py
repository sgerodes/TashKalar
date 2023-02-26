import metadata


class MetadataManager:
    _card_type_and_card_name_2_manual_metadata = None
    _card_type_and_card_name_2_image_indexes = None

    @staticmethod
    def get_manual_metadata_for_card(card_type, card_name) -> dict:
        return MetadataManager._card_type_and_card_name_2_manual_metadata[card_type][card_name]

    @staticmethod
    def get_index_in_big_image_for_card(card_type, card_name) -> int:
        return MetadataManager._card_type_and_card_name_2_image_indexes[card_type][card_name]

    @staticmethod
    def get_fetched_metadata_for_card(card_type, card_name):
        return metadata.all_fetched_metadata[card_type][card_name]


def populate_internal_dicts():
    MetadataManager._card_type_and_card_name_2_manual_metadata = dict()
    MetadataManager._card_type_and_card_name_2_image_indexes = dict()
    for card_type, metadata_ordered in metadata.all_manual_metadata_ordered.items():
        MetadataManager._card_type_and_card_name_2_manual_metadata[card_type] = dict()
        MetadataManager._card_type_and_card_name_2_image_indexes[card_type] = dict()
        for i, card_metadata in enumerate(metadata_ordered):
            # card_type_and_card_name_2_manual_metadata
            MetadataManager._card_type_and_card_name_2_manual_metadata[card_type][card_metadata['name']] = card_metadata
            # card_type_and_card_name_2_image_indexes
            MetadataManager._card_type_and_card_name_2_image_indexes[card_type][card_metadata['name']] = i


populate_internal_dicts()
