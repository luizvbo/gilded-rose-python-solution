import pytest

from gilded_rose.gilded_rose import GildedRose, Item


@pytest.fixture
def compare_item_after_update():
    def _compare_item_after_update(
        name, sell_in_before, quality_before, sell_in_after, quality_after
    ):
        gild_rose = GildedRose((Item(name, sell_in_before, quality_before),))
        gild_rose.update_quality()
        assert (
            gild_rose.items[0].__dict__
            == Item(name, sell_in_after, quality_after).__dict__
        )

    return _compare_item_after_update
