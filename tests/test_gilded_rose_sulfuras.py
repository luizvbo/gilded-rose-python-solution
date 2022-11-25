item_name = "Sulfuras, Hand of Ragnaros"


def test_update_quality(compare_item_after_update):
    compare_item_after_update(item_name, 11, 2, 11, 2)
