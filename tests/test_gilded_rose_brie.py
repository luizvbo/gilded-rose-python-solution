from gilded_rose.gilded_rose import item_types

item_name = item_types.brie


def test_increase_quality(compare_item_after_update):
    compare_item_after_update(item_name, 11, 2, 10, 3)


def test_increase_quality_over_max(compare_item_after_update):
    compare_item_after_update(item_name, 2, 50, 1, 50)


def test_increase_quality_by_2(compare_item_after_update):
    compare_item_after_update(item_name, 0, 4, -1, 6)


def test_increase_quality_by_2_over_max(compare_item_after_update):
    compare_item_after_update(item_name, 0, 50, -1, 50)


def test_increase_quality_by_1_plus_1_over_max(compare_item_after_update):
    compare_item_after_update(item_name, 0, 49, -1, 50)
