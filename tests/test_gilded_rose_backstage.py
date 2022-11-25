
item_name = "Backstage passes to a TAFKAL80ETC concert"

def test_increase_quality_gt_10_days(compare_item_after_update):
    compare_item_after_update(item_name, 11, 2, 10, 3)

def test_increase_quality_gt_10_days_over_max(compare_item_after_update):
    compare_item_after_update(item_name, 11, 50, 10, 50)

def test_increase_quality_gt_5_days(compare_item_after_update):
    compare_item_after_update(item_name, 9, 2, 8, 4)

def test_increase_quality_gt_5_days_over_max(compare_item_after_update):
    compare_item_after_update(item_name, 9, 50, 8, 50)

def test_increase_quality_le_5_days(compare_item_after_update):
    compare_item_after_update(item_name, 5, 2, 4, 5)

def test_increase_quality_le_5_days_over_max(compare_item_after_update):
    compare_item_after_update(item_name, 5, 50, 4, 50)

def test_increase_quality_le_0_days(compare_item_after_update):
    compare_item_after_update(item_name, 0, 5, -1, 0)

def test_increase_quality_le_0_days_keep_0(compare_item_after_update):
    compare_item_after_update(item_name, -1, 0, -2, 0)