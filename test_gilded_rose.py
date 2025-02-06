# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    ###def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEquals(80, sulfuras_item.quality)
        self.assertEquals(4, sulfuras_item.sell_in)
        self.assertEquals("Sulfuras", sulfuras_item.name)
    
    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEquals(["Sulfuras"], all_items)

    def test_quality_degrades_twice_as_fast_after_sell_by_date(self):
        """Test that quality degrades twice as fast after the sell by date has passed"""
        # Arrange
        items = [Item("standard item", 0, 10)]  # SellIn of 0 means sell-by date has passed
        gilded_rose = GildedRose(items)
        
        # Act
        gilded_rose.update_quality()
        
        # Assert
        # Quality should decrease by 2 since sell-by date has passed
        self.assertEqual(8, items[0].quality, 
            "Quality should degrade twice as fast after sell-by date")
    
    def test_conjured_items_degrade_twice_as_fast(self):
        """Test that conjured items degrade in quality twice as fast as normal items"""
        # Arrange
        items = [
            Item("Conjured Mana Cake", 3, 10),  # Conjured item
            Item("standard item", 3, 10)         # Normal item for comparison
        ]
        gilded_rose = GildedRose(items)
        
        # Act
        gilded_rose.update_quality()
        
        # Assert
        self.assertEqual(8, items[0].quality, 
            "Conjured items should degrade twice as fast")
        self.assertEqual(9, items[1].quality, 
            "Normal items should degrade by 1")
    
    def test_backstage_passes_quality_increases(self):
        """Test that backstage passes increase in quality as sell-in approaches"""
        # Arrange
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 11, 20),  # Regular increase
            Item("Backstage passes to a TAFKAL80ETC concert", 10, 20),  # Should increase by 2
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 20),   # Should increase by 3
            Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)    # Should drop to 0
        ]
        gilded_rose = GildedRose(items)
        
        # Act
        gilded_rose.update_quality()
        
        # Assert
        self.assertEqual(21, items[0].quality, "Quality should increase by 1 when more than 10 days")
        self.assertEqual(22, items[1].quality, "Quality should increase by 2 when 10 days or less")
        self.assertEqual(23, items[2].quality, "Quality should increase by 3 when 5 days or less")
        self.assertEqual(0, items[3].quality, "Quality should drop to 0 after concert")
    
    def test_get_item_categories(self):
        """Test getting a list of all unique item categories in the store (syntax error test)"""
        # Arrange
        items = [
            Item("Aged Brie", 2, 0),
            Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
            Item("Sulfuras, Hand of Ragnaros", 0, 80),
            Item("Conjured Mana Cake", 3, 6)
        ]
        gilded_rose = GildedRose(items)
        
        # Act & Assert
        # This should fail because get_item_categories() method doesn't exist
        categories = gilded_rose.get_item_categories()
        self.assertEqual(
            ["Aged Brie", "Backstage passes", "Sulfuras", "Conjured"], 
            categories,
            "Should return list of unique item categories"
        )


if __name__ == '__main__':
    unittest.main()
