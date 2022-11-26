"""Main module with the logic used to update the item information"""
from types import SimpleNamespace
from typing import Iterable

# Item names used across the code
item_types = SimpleNamespace(
    brie="Aged Brie",
    backstage_passes="Backstage passes to a TAFKAL80ETC concert",
    sulfuras="Sulfuras, Hand of Ragnaros",
    regular="Elixir of the Mongoose",
    conjured="Conjured Mana Cake",
)


class Item:  # pylint: disable=too-few-public-methods
    """Data class used to store information about the goods"""

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"


class GildedRose:
    """Main class responsible for keeping and updating the items"""

    def __init__(self, items: Iterable[Item]):
        self.items = items

    def update_quality(self):
        """Update the quality of the items."""
        for item in self.items:
            self.update_item(item)

    def update_item(self, item: Item):
        """Update an item according to its type.

        At the end, the method makes sure that the quality is never negative or
        greater than 50. With this, we can remove the manual checks for the
        upper/lower bounds for the item quality.

        Args:
            item (Item): Item to be updated.
        """

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

        # Make sure the quality constraints are respected.
        item.quality = min(50, max(0, quality))

    def update_brie(self, item: Item) -> int:
        """Update 'Aged Brie' items.

        Args:
            item (Item): Item to be updated.

        Returns:
            int: The updated quality of the item.
        """
        quality = item.quality + 1
        item.sell_in -= 1
        if item.sell_in < 0:
            quality += 1
        return quality

    def update_backstage(self, item: Item) -> int:
        """Update 'Backstage passes' items.

        Args:
            item (Item): Item to be updated.

        Returns:
            int: The updated quality of the item.
        """
        quality = item.quality + 1
        if item.sell_in < 11:
            quality += 1
        if item.sell_in < 6:
            quality += 1
        item.sell_in -= 1
        if item.sell_in < 0:
            quality = 0
        return quality

    def update_sulfurus(self, item: Item) -> int:
        """Update 'Sulfuras' items.

        Args:
            item (Item): Item to be updated.

        Returns:
            int: The updated quality of the item.
        """
        return item.quality

    def update_regular(self, item: Item, decrement: int = 1) -> int:
        """Update 'regular' items.

        Args:
            item (Item): Item to be updated.

        Returns:
            int: The updated quality of the item.
        """
        quality = item.quality - decrement
        item.sell_in -= 1
        if item.sell_in < 0:
            quality -= decrement
        return quality

    def update_conjuured(self, item: Item) -> int:
        """Update 'Conjured' items.

        Args:
            item (Item): Item to be updated.

        Returns:
            int: The updated quality of the item.
        """
        return self.update_regular(item, decrement=2)
