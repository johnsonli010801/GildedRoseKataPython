# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(5, sulfuras_item.sell_in)  # Sulfuras sell_in should not decrease
        self.assertEqual("Sulfuras, Hand of Ragnaros", sulfuras_item.name)

    
    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEqual(["Sulfuras, Hand of Ragnaros"], all_items)

    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 0, 20)]  # Aged Brie on the sell-by date
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality, 
                        "Aged Brie should increase in quality twice as fast after sell-by date")


    # Logical Error Test 2: Testing Backstage Pass quality rules
    def test_backstage_pass_quality_increases(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        pass_item = items[0]
        self.assertEqual(23, pass_item.quality,  # Expect an increase by 3
                        "Backstage pass should increase by 3 when SellIn is 5 days or less")


    def test_conjured_items_degrade_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality,  # Degrades by 2 when sell_in is not below 0
                        "Conjured items should degrade by 2 quality per day")


    # Syntax Error Test: Testing non-existent method
    def test_get_items_by_quality_threshold(self):
        items = [
            Item("Sulfuras", 5, 80),
            Item("Aged Brie", 10, 20),
            Item("Normal Item", 15, 30)
        ]
        gilded_rose = GildedRose(items)
        high_quality_items = gilded_rose.get_items_by_quality_threshold(50)
        self.assertEqual(1, len(high_quality_items),
                        "Should return items with quality above the threshold")


if __name__ == '__main__':
    unittest.main()
