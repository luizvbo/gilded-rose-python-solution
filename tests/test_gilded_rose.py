from gilded_rose_app.gilded_rose import GildedRose, Item


def test_item_name():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert "foo" == items[0].name


def test_item_as_string():
    item = Item("foo", 0, 0)
    assert str(item) == f"{item.name}, {item.sell_in}, {item.quality}"
