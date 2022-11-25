from gilded_rose.gilded_rose import item_types
item_name = item_types.regular


def test_decrease_quality(compare_item_after_update):
    compare_item_after_update(item_name, 11, 4, 10, 3)

def test_decrease_quality_always_0(compare_item_after_update):
    compare_item_after_update(item_name, 11, 0, 10, 0)

def test_decrease_quality_expired(compare_item_after_update):
    compare_item_after_update(item_name, -1, 2, -2, 0)
