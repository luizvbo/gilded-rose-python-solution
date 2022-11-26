from gilded_rose_app.gilded_rose import item_types

item_name = item_types.conjured


def test_decrease_quality_by_2(compare_item_after_update):
    compare_item_after_update(item_name, 11, 4, 10, 2)


def test_decrease_quality_by_2_after_expired(compare_item_after_update):
    compare_item_after_update(item_name, 0, 4, -1, 0)
