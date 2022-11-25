# -*- coding: utf-8 -*-
from typing import Iterable
from types import SimpleNamespace

item_types = SimpleNamespace(
    brie="Aged Brie",
    backstage_passes="Backstage passes to a TAFKAL80ETC concert",
    sulfuras="Sulfuras, Hand of Ragnaros",
    regular="Elixir of the Mongoose",
    conjured="Conjured Mana Cake",
)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):
    def __init__(self, items: Iterable[Item]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_item(item)

    def update_item(self, item: Item):
        if item.name == item_types.brie:
            quality = self.update_brie(item)
        elif item.name == item_types.backstage_passes:
            quality = self.update_backstage(item)
        elif item.name == item_types.sulfuras:
            quality = self.update_sulfurus(item)
        elif item.name == item_types.conjured:
            quality = self.update_conjuured(item)
        else:
            quality = self.update_regular(item)

        # Make sure the quality constraints are respected
        if quality < 0:
            quality = 0
        if quality > 50:
            quality = 50
        item.quality = quality

    def update_brie(self, item: Item):
        quality = item.quality + 1
        item.sell_in -= 1
        if item.sell_in < 0:
            quality += 1
        return quality

    def update_backstage(self, item: Item):
        quality = item.quality + 1
        if item.sell_in < 11:
            quality += 1
        if item.sell_in < 6:
            quality += 1
        item.sell_in -= 1
        if item.sell_in < 0:
            quality = 0
        return quality

    def update_sulfurus(self, item: Item):
        return item.quality

    def update_regular(self, item: Item, decrement: int=1):
        quality = item.quality - decrement
        item.sell_in -= 1
        if item.sell_in < 0:
            quality -= decrement
        return quality

    def update_conjuured(self, item: Item):
        return self.update_regular(item, decrement=2)
