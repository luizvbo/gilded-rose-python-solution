# -*- coding: utf-8 -*-
from gilded_rose.gilded_rose import Item, GildedRose


def test_item_name():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert "foo"==items[0].name

def test_item_as_string():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    assert str(items[0]) == f"{items[0].name}, {items[0].sell_in}, {items[0].quality}"
